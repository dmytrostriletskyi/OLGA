#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utils for functional tests.
"""

from datetime import datetime
import pytz

from mock import patch

from django.test import TestCase

from olga.analytics.tests.factories import InstallationStatisticsFactory


class SetUp(TestCase):
    """
    Common setup for functional tests cases.
    """

    @staticmethod
    def setUp():  # pylint: disable=invalid-name
        """
        Create one installation statistics object with factory data.
        """
        mock_data_created_datetime = datetime(2017, 7, 5, 20, 25, 23, 259923, pytz.UTC)

        with patch('django.utils.timezone.now') as mock_timezone_now:

            mock_timezone_now.return_value = mock_data_created_datetime

            InstallationStatisticsFactory(data_created_datetime=mock_data_created_datetime)


class _HtmlTargets(object):
    """
    Contains several acceptor parts of html-templates, that need to be tested.
    """

    def __init__(self):
        """
        Init for HtmlTargets.
        """
        self._activity_metric = \
            '<div class="summary-point-wrapper">' \
            '<div class="summary-point-number" title="{0}">{0}</div>' \
            '<div class="summary-point-label">{1}</div>' \
            '</div>'

        self._country_grid_cell = '<td role="gridcell">{0}</td>'
        self._country_count_grid_cell = '<td class="text-right sorting_1" role="gridcell">{0}</td>'
        self._percentage = '<td class="text-right" role="gridcell">{0}</td>'

        self._extraction_duration = \
            '<a href="#" id="olga-dates" class="navbar-link active-course-name">' \
            'Open edX Learners Global Analytics for {0} — {1}</a>'
        self._course_engagement_last_update = \
            '<div class="data-update-message">Course engagement data was last updated {0} at {1} UTC+2.</div>'

    @property
    def activity_metric(self):
        """
        Return activity metric part, that contains activity metric count and label testing parameters.
        """
        return self._activity_metric

    @property
    def country_grid_cell(self):
        """
        Return geographic breakdown table first `td` part, that contains country count testing parameter.
        """
        return self._country_grid_cell

    @property
    def country_count_grid_cell(self):
        """
        Return geographic breakdown table second `td` part, that contains country count testing parameter.
        """
        return self._country_count_grid_cell

    @property
    def percentage_grid_cell(self):
        """
        Return geographic breakdown table third `td` part, that contains percentage testing parameter.
        """
        return self._percentage

    @property
    def extraction_duration(self):
        """
        Return extraction duration part, that contains dates testing parameters.
        """
        return self._extraction_duration

    @property
    def course_engagement_last_update(self):
        """
        Return course engagement last update part, that contains date testing parameters.
        """
        return self._course_engagement_last_update


html_target = _HtmlTargets()  # pylint: disable=invalid-name