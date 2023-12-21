#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/9/19 20:39
@Author  : femto Zheng
@File    : get_template.py
"""
from metagpt.config import CONFIG


def get_template(templates, schema=CONFIG.prompt_schema):
    selected_templates = templates.get(schema)
    if selected_templates is None:
        raise ValueError(f"Can't find {schema} in passed in templates")

    # Extract the selected templates
    prompt_template = selected_templates["PROMPT_TEMPLATE"]
    format_example = selected_templates["FORMAT_EXAMPLE"]

    return prompt_template, format_example
