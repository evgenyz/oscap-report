# Copyright 2022, Red Hat, Inc.
# SPDX-License-Identifier: LGPL-2.1-or-later

import pytest

from openscap_report.debug_settings import DebugSetting


@pytest.mark.parametrize("debug_flags, expected_values", [
    (
        [
            "NO-MINIFY",
            "BUTTON-SHOW-ALL-RULES",
            "ONLINE-CSS",
            "BUTTON-SHOW-ALL-RULES-AND-OVAL-TEST-DETAILS"
        ],
        DebugSetting(
            no_minify=True,
            include_debug_script=True,
            button_show_all_rules=True,
            use_online_css=True,
            button_show_all_rules_and_oval_test_details=True
        )
    ),
    (
        [
            "BUTTON-SHOW-ALL-RULES",
            "ONLINE-CSS",
            "BUTTON-SHOW-ALL-RULES-AND-OVAL-TEST-DETAILS"
        ],
        DebugSetting(
            include_debug_script=True,
            button_show_all_rules=True,
            use_online_css=True,
            button_show_all_rules_and_oval_test_details=True
        )
    ),
    (
        [
            "NO-MINIFY",
            "ONLINE-CSS",
            "BUTTON-SHOW-ALL-RULES-AND-OVAL-TEST-DETAILS"
        ],
        DebugSetting(
            no_minify=True,
            include_debug_script=True,
            use_online_css=True,
            button_show_all_rules_and_oval_test_details=True
        )
    ),
    (
        [
            "NO-MINIFY",
            "BUTTON-SHOW-ALL-RULES",
            "BUTTON-SHOW-ALL-RULES-AND-OVAL-TEST-DETAILS"
        ],
        DebugSetting(
            no_minify=True,
            include_debug_script=True,
            button_show_all_rules=True,
            button_show_all_rules_and_oval_test_details=True
        )
    ),
    (
        [
            "NO-MINIFY",
            "BUTTON-SHOW-ALL-RULES",
            "ONLINE-CSS",
        ],
        DebugSetting(
            no_minify=True,
            include_debug_script=True,
            button_show_all_rules=True,
            use_online_css=True,
        )
    ),
    (
        [
            "NO-MINIFY",
            "ONLINE-CSS",
        ],
        DebugSetting(
            no_minify=True,
            use_online_css=True,
        )
    ),
    (
        [
            "NO-MINIFY",
        ],
        DebugSetting(
            no_minify=True,
        )
    ),
    (
        [
            "BUTTON-SHOW-ALL-RULES",
        ],
        DebugSetting(
            include_debug_script=True,
            button_show_all_rules=True,
        )
    ),
    (
        [
            "ONLINE-CSS",
        ],
        DebugSetting(
            use_online_css=True,
        )
    ),
    (
        [
            "BUTTON-SHOW-ALL-RULES-AND-OVAL-TEST-DETAILS"
        ],
        DebugSetting(
            include_debug_script=True,
            button_show_all_rules_and_oval_test_details=True
        )
    ),
    (
        [],
        DebugSetting()
    ),
])
def test_update_settings_with_debug_flags(debug_flags, expected_values):
    debug_settings = DebugSetting()
    debug_settings.update_settings_with_debug_flags(debug_flags)
    assert expected_values == debug_settings
