"""Tests for Zabbix Datasource"""

from io import StringIO

import grafanalib.core as G
import grafanalib.zabbix as Z
from grafanalib import _gen


def test_serialization_zabbix_target():
    """Serializing a graph doesn't explode."""
    graph = G.Graph(
        title="CPU Usage",
        dataSource="Zabbix data source",
        targets=[
            Z.zabbixMetricTarget(
                group="Zabbix Group",
                host="Zabbix Host",
                application="CPU",
                item="/CPU (load)/",
                functions=[
                    Z.ZabbixSetAliasFunction("View alias"),
                ]),
        ],
        id=1,
        yAxes=[
            G.YAxis(format=G.SHORT_FORMAT, label="CPU seconds / second"),
            G.YAxis(format=G.SHORT_FORMAT),
        ],
    )
    stream = StringIO()
    _gen.write_dashboard(graph, stream)
    assert stream.getvalue() != ''