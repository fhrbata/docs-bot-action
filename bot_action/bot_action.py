#!/usr/bin/env python
#
# SPDX-FileCopyrightText: 2025 Espressif Systems (Shanghai) CO LTD
#
# SPDX-License-Identifier: Apache-2.0

import argparse
import json
import os
import requests


def get_suggestion(issue_body: str) -> str:
    return 'THIS IS MOCKED ANSWER'

def get_suggestion_old(issue_body: str) -> str:
    payload = json.dumps({'integration_id': os.environ['BOT_INTEGRATION_ID'], 'query': issue_body})

    headers = {'content-type': 'application/json', 'X-API-KEY': os.environ['BOT_API_KEY']}
    r = requests.post(os.environ['BOT_API_ENDPOINT'], data=payload, headers=headers)

    r.raise_for_status()
    j = r.json()
    try:
        answer = j['answer']
    except KeyError:
        raise RuntimeError(str(j))

    assert isinstance(answer, str), 'No answer found'

    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, default=None)
    args = parser.parse_args()

    if args.input_file:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            print(get_suggestion(f.read()))


if __name__ == '__main__':
    main()
