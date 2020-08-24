#!/usr/bin/env bash

python -m pytest --cov=gitstats --cov-branch --cov-report term-missing --cov-fail-under=90