#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from json import dump, loads
from pathlib import Path

import click
from bs4 import BeautifulSoup
from requests import get

BASE_URL = "https://developer.redoxengine.com/data-models"
MODEL_LIST = [
    "ClinicalSummary",
    "ClinicalDecisions",
    "Claim",
    "Device",
    "Enrichment",
    "Financial",
    "Flowsheet",
    "Inventory",
    "Medications",
    "Media",
    "Notes",
    "Order",
    "Organization",
    "PatientAdmin",
    "PatientEducation",
    "PatientSearch",
    "Provider",
    "Referral",
    "Research",
    "Results",
    "Scheduling",
    "SSO",
    "SurgicalScheduling",
    "Vaccination",
]
FIXTURE_DIR = Path(__file__).parent / "fixtures"


def get_http(model: str) -> BeautifulSoup:
    resp = get(
        f"{BASE_URL}/{model}.html",
        headers={
            "User-Agent": "PostmanRuntime/7.29.0",
            "Accept-Encoding": "gzip, deflate, br",
        },
    )

    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def find_sample(http: BeautifulSoup) -> str:
    for pre in http.find_all("pre", "redox-model"):
        yield pre.text


def save_fixture(sample: str):
    sample_dict = loads(
        sample, object_hook=lambda d: {k: v for k, v in d.items() if v is not None}
    )  # Hook removes any None values from the dict

    model: str = sample_dict["Meta"]["DataModel"].lower()
    event: str = sample_dict["Meta"]["EventType"].lower().replace("-", "")
    fixture_file_name = f"{model}_{event}.json"

    dest_file = FIXTURE_DIR / fixture_file_name
    with open(dest_file, "w") as fixture_file:
        click.echo(f"Writing file {dest_file}")
        dump(sample_dict, fixture_file, indent=2)


@click.command()
def main():
    for model in MODEL_LIST:
        click.echo(f"\nGetting HTTP data for the {model} model")
        http = get_http(model)
        for sample in find_sample(http):
            save_fixture(sample)


if __name__ == "__main__":
    main()
