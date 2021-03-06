<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEBME6099FinalProject" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(44.0, 466.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="c9210641-7d00-42eb-a256-9d18414df4ee" version="1.0.0" />
		<node id="1" name="Spectrum Plot" position="(439.0, 325.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" title="Spectrum Plot" uuid="a5b0dc25-72c5-4e2c-9bec-318eb75f8188" version="1.0.0" />
		<node id="2" name="Power Spectrum (Welch)" position="(278.0, 261.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owwelchspectrum.OWWelchSpectrum" title="Power Spectrum (Welch)" uuid="09f8c3ac-c12a-4c07-9777-5d7b4ab80be7" version="1.0.0" />
		<node id="3" name="Inspect Data" position="(431.0, 218.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data (1)" uuid="c629bbfc-abed-4f59-a653-b12c8d61c28e" version="2.1.1" />
		<node id="4" name="Dejitter Timestamps" position="(178.0, 453.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="b9f0bd20-20a6-4be3-adf2-0bccd08dd727" version="1.0.0" />
		<node id="5" name="Assign Target Values" position="(269.0, 525.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Target Values" uuid="0f8af791-c788-4a5b-b49b-1921ae867e79" version="1.0.0" />
		<node id="6" name="Segmentation" position="(442.0, 470.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="3201365f-ee8e-43f5-b9e8-fff5336d8532" version="1.0.1" />
		<node id="7" name="Inspect Data" position="(182.0, 630.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data (2)" uuid="094e2f6f-c4d5-43ae-8ad5-5736298e30b1" version="2.1.1" />
		<node id="8" name="LSL Output" position="(577.0, 605.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="e00c40f6-e7f3-4d5c-80a1-93605c2ca84b" version="1.0.0" />
		<node id="9" name="Inspect Data" position="(541.0, 423.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data" uuid="54419917-cf72-4f7b-a42d-9f41bd7bedb0" version="2.1.1" />
		<node id="10" name="FIR Filter" position="(350.0, 420.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="63a9b6d9-8900-4da3-bbae-89043227d203" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="2" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQIoWAMAAABGcDFxA1gDAAAARnAycQRYAwAAAEFG
N3EFWAMAAABBRjNxBlgDAAAAQUY0cQdYAwAAAEFGOHEIWAIAAABGN3EJWAIAAABGNXEKWAIAAABG
M3ELWAIAAABGMXEMWAIAAABGenENWAIAAABGMnEOWAIAAABGNHEPWAIAAABGNnEQWAIAAABGOHER
WAMAAABGVDdxElgDAAAARkM1cRNYAwAAAEZDM3EUWAMAAABGQzFxFVgDAAAARkN6cRZYAwAAAEZD
MnEXWAMAAABGQzRxGFgDAAAARkM2cRlYAwAAAEZUOHEaWAIAAABUN3EbWAIAAABDNXEcWAIAAABD
M3EdWAIAAABDMXEeWAIAAABDenEfWAIAAABDMnEgWAIAAABDNHEhWAIAAABDNnEiWAIAAABUOHEj
WAMAAABUUDdxJFgDAAAAQ1A1cSVYAwAAAENQM3EmWAMAAABDUDFxJ1gDAAAAQ1B6cShYAwAAAENQ
MnEpWAMAAABDUDRxKlgDAAAAQ1A2cStYAwAAAFRQOHEsWAIAAABQN3EtWAIAAABQNXEuWAIAAABQ
M3EvWAIAAABQMXEwWAIAAABQenExWAIAAABQMnEyWAIAAABQNHEzWAIAAABQNnE0WAIAAABQOHE1
WAMAAABQTzdxNlgDAAAAUE96cTdYAwAAAFBPOHE4WAIAAABPMXE5WAIAAABPMnE6ZVgLAAAAZGlh
Z25vc3RpY3NxO4lYDAAAAG1hcmtlcl9xdWVyeXE8WCAAAABuYW1lPSdORVJfMjAxNV9CQ0lfQ2hh
bGxlbmdlX0VNJ3E9WAwAAABtYXhfYmxvY2tsZW5xPk0ABFgKAAAAbWF4X2J1ZmxlbnE/Sx5YDAAA
AG1heF9jaHVua2xlbnFASwBYDAAAAG5vbWluYWxfcmF0ZXFBWA0AAAAodXNlIGRlZmF1bHQpcUJY
BQAAAHF1ZXJ5cUNYIQAAAG5hbWU9J05FUl8yMDE1X0JDSV9DaGFsbGVuZ2VfRUVHJ3FEWAcAAABy
ZWNvdmVycUWIWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXFGRz/gAAAAAAAAWBMAAABzYXZlZFdp
ZGdldEdlb21ldHJ5cUdjc2lwCl91bnBpY2tsZV90eXBlCnFIWAwAAABQeVF0NC5RdENvcmVxSVgK
AAAAUUJ5dGVBcnJheXFKQy4B2dDLAAEAAAAAAycAAAKcAAAEngAAA4IAAAMvAAACuwAABJYAAAN6
AAAAAAAAcUuFcUyHcU1ScU5YDgAAAHNldF9icmVha3BvaW50cU+JdS4=
</properties>
		<properties format="literal" node_id="1">{'always_on_top': False, 'antialiased': True, 'autoscale': True, 'background_color': '#FFFFFF', 'decoration_color': '#000000', 'downsampled': False, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'line_width': 0.75, 'one_over_f_correction': False, 'savedWidgetGeometry': None, 'scale': 1.0, 'set_breakpoint': False, 'stacked': True, 'stream_name': '(use default)', 'title': 'Spectrum view', 'zero_color': '#7F7F7F7F'}</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWBgAAABhdmVyYWdlX292ZXJfdGltZV93aW5kb3dxAYlYBAAAAGF4aXNxAlgEAAAAdGlt
ZXEDWAcAAABkZXRyZW5kcQRYCAAAAGNvbnN0YW50cQVYCAAAAGZmdF9zaXplcQZYDQAAACh1c2Ug
ZGVmYXVsdClxB1gIAAAAb25lc2lkZWRxCIhYDwAAAG92ZXJsYXBfc2FtcGxlc3EJaAdYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxCmNzaXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ0LlF0Q29y
ZXEMWAoAAABRQnl0ZUFycmF5cQ1DLgHZ0MsAAQAAAAAFLgAAAtAAAAalAAADgwAABTYAAALvAAAG
nQAAA3sAAAAAAABxDoVxD4dxEFJxEVgHAAAAc2NhbGluZ3ESWAcAAABkZW5zaXR5cRNYDwAAAHNl
Z21lbnRfc2FtcGxlc3EUaAdYDgAAAHNldF9icmVha3BvaW50cRWJWAQAAAB1bml0cRZYBwAAAHNh
bXBsZXNxF1gGAAAAd2luZG93cRhYBAAAAGhhbm5xGXUu
</properties>
		<properties format="literal" node_id="3">{'always_on_top': True, 'auto_close': False, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': True, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlj
a2xlX3R5cGUKcQVYDAAAAFB5UXQ0LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAA
AAAEcgAAAo0AAAXpAAAC+wAABHoAAAKsAAAF4QAAAvMAAAAAAABxCIVxCYdxClJxC1gOAAAAc2V0
X2JyZWFrcG9pbnRxDIlYDgAAAHdhcm11cF9zYW1wbGVzcQ1K/////3Uu
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYCQAAAGluY29ycmVj
dHEHSwFYBwAAAGNvcnJlY3RxCEsAdVgOAAAAbWFwcGluZ19mb3JtYXRxCVgGAAAAY29tcGF0cQpY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxC2NzaXAKX3VucGlja2xlX3R5cGUKcQxYDAAAAFB5UXQ0
LlF0Q29yZXENWAoAAABRQnl0ZUFycmF5cQ5DLgHZ0MsAAQAAAAAF1QAAAoAAAAdMAAADMwAABd0A
AAKfAAAHRAAAAysAAAAAAABxD4VxEIdxEVJxElgOAAAAc2V0X2JyZWFrcG9pbnRxE4lYEQAAAHN1
cHBvcnRfd2lsZGNhcmRzcRSJWAsAAAB1c2VfbnVtYmVyc3EViVgHAAAAdmVyYm9zZXEWiXUu
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgPAAAAb25saW5lX2Vwb2NoaW5ncQNYDQAAAG1hcmtlci1sb2NrZWRxBFgNAAAAc2FtcGxl
X29mZnNldHEFSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUK
cQdYDAAAAFB5UXQ0LlF0Q29yZXEIWAoAAABRQnl0ZUFycmF5cQlDLgHZ0MsAAQAAAAAEcgAAAkgA
AAXpAAADQAAABHoAAAJnAAAF4QAAAzgAAAAAAABxCoVxC4dxDFJxDVgOAAAAc2VsZWN0X21hcmtl
cnNxDlgNAAAAKHVzZSBkZWZhdWx0KXEPWA4AAABzZXRfYnJlYWtwb2ludHEQiVgLAAAAdGltZV9i
b3VuZHNxEV1xEihK9v///0sAZVgHAAAAdmVyYm9zZXETiHUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGIWAoAAABhdXRvX2Nsb3NlcQKJWAgAAABjb2xfYXhp
c3EDWAQAAAB0aW1lcQRYCAAAAGRlY2ltYWxzcQVLBlgNAAAAZXZlcnlfbl90aWNrc3EGSwFYDQAA
AGZld2VyX2J1dHRvbnNxB4hYCQAAAGZvbnRfc2l6ZXEISwpYEAAAAGluaXRpYWxfcG9zaXRpb25x
CV1xCihLFEsyTfQBTZABZVgIAAAAcm93X2F4aXNxC1gFAAAAc3BhY2VxDFgTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXENY3NpcApfdW5waWNrbGVfdHlwZQpxDlgMAAAAUHlRdDQuUXRDb3JlcQ9YCgAA
AFFCeXRlQXJyYXlxEEMuAdnQywABAAAAAARyAAACEQAABekAAAN4AAAEegAAAjAAAAXhAAADcAAA
AAAAAHERhXESh3ETUnEUWA4AAABzZXRfYnJlYWtwb2ludHEViVgPAAAAc2hvd19heGVzX3RhYmxl
cRaIWA8AAABzaG93X2RhdGFfdGFibGVxF4hYEgAAAHNob3dfbWFya2Vyc190YWJsZXEYiFgQAAAA
c2hvd19tYXhfY29sdW1uc3EZSxRYDwAAAHNob3dfbWF4X3ZhbHVlc3EaSzJYEgAAAHNob3dfc3Ry
ZWFtc190YWJsZXEbiFgLAAAAc3RyZWFtX25hbWVxHFgNAAAAKHVzZSBkZWZhdWx0KXEdWAwAAAB3
aW5kb3dfdGl0bGVxHlgTAAAASW5zcGVjdCBEYXRhIFBhY2tldHEfdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAABHIAAAIFAAAF6QAA
A4QAAAR6AAACJAAABeEAAAN8AAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETaAZYBQAAAHNyYXRlcRRYDQAAACh1
c2UgZGVmYXVsdClxFVgLAAAAc3RyZWFtX25hbWVxFlgeAAAATkVSXzIwMTVfQkNJX0NoYWxsZW5n
ZV9TYW1wbGVzcRdYCwAAAHN0cmVhbV90eXBlcRhYBwAAAENvbnRyb2xxGVgTAAAAdXNlX2RhdGFf
dGltZXN0YW1wc3EaiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEbiXUu
</properties>
		<properties format="literal" node_id="9">{'always_on_top': True, 'auto_close': False, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': True, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEc/0AAAAAAAAEc/4AAAAAAAAEsPSxBlWA0AAABtaW5pbXVtX3Bo
YXNlcQmIWAQAAABtb2RlcQpYCAAAAGJhbmRwYXNzcQtYBQAAAG9yZGVycQxYDQAAACh1c2UgZGVm
YXVsdClxDVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEOY3NpcApfdW5waWNrbGVfdHlwZQpxD1gM
AAAAUHlRdDQuUXRDb3JlcRBYCgAAAFFCeXRlQXJyYXlxEUMuAdnQywABAAAAAARyAAACawAABekA
AAMeAAAEegAAAooAAAXhAAADFgAAAAAAAHEShXETh3EUUnEVWA4AAABzZXRfYnJlYWtwb2ludHEW
iVgKAAAAc3RvcF9hdHRlbnEXR0BJAAAAAAAAdS4=
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node3",
            "data",
            "node4",
            "data"
        ],
        [
            "node3",
            "data",
            "node2",
            "data"
        ],
        [
            "node1",
            "data",
            "node5",
            "data"
        ],
        [
            "node1",
            "data",
            "node8",
            "data"
        ],
        [
            "node1",
            "data",
            "node3",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data"
        ],
        [
            "node7",
            "data",
            "node9",
            "data"
        ],
        [
            "node7",
            "data",
            "node10",
            "data"
        ],
        [
            "node6",
            "data",
            "node11",
            "data"
        ],
        [
            "node11",
            "data",
            "node7",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Fp1",
                        "Fp2",
                        "AF7",
                        "AF3",
                        "AF4",
                        "AF8",
                        "F7",
                        "F5",
                        "F3",
                        "F1",
                        "Fz",
                        "F2",
                        "F4",
                        "F6",
                        "F8",
                        "FT7",
                        "FC5",
                        "FC3",
                        "FC1",
                        "FCz",
                        "FC2",
                        "FC4",
                        "FC6",
                        "FT8",
                        "T7",
                        "C5",
                        "C3",
                        "C1",
                        "Cz",
                        "C2",
                        "C4",
                        "C6",
                        "T8",
                        "TP7",
                        "CP5",
                        "CP3",
                        "CP1",
                        "CPz",
                        "CP2",
                        "CP4",
                        "CP6",
                        "TP8",
                        "P7",
                        "P5",
                        "P3",
                        "P1",
                        "Pz",
                        "P2",
                        "P4",
                        "P6",
                        "P8",
                        "PO7",
                        "POz",
                        "PO8",
                        "O1",
                        "O2"
                    ]
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='NER_2015_BCI_Challenge_EM'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='NER_2015_BCI_Challenge_EEG'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c9210641-7d00-42eb-a256-9d18414df4ee"
        },
        "node10": {
            "class": "InspectData",
            "module": "neuropype.nodes.visualization.InspectData",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_close": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 6
                },
                "every_n_ticks": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "fewer_buttons": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "font_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "initial_position": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        20,
                        50,
                        500,
                        400
                    ]
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_axes_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_data_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_markers_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "54419917-cf72-4f7b-a42d-9f41bd7bedb0"
        },
        "node11": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.25,
                        0.5,
                        15,
                        16
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "63a9b6d9-8900-4da3-bbae-89043227d203"
        },
        "node2": {
            "class": "SpectrumPlot",
            "module": "neuropype.nodes.visualization.SpectrumPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "one_over_f_correction": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stacked": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Spectrum view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F7F"
                }
            },
            "uuid": "a5b0dc25-72c5-4e2c-9bec-318eb75f8188"
        },
        "node3": {
            "class": "WelchSpectrum",
            "module": "neuropype.nodes.spectral.WelchSpectrum",
            "params": {
                "average_over_time_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "detrend": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "constant"
                },
                "fft_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "onesided": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "overlap_samples": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "scaling": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "density"
                },
                "segment_samples": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "samples"
                },
                "window": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "hann"
                }
            },
            "uuid": "09f8c3ac-c12a-4c07-9777-5d7b4ab80be7"
        },
        "node4": {
            "class": "InspectData",
            "module": "neuropype.nodes.visualization.InspectData",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_close": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 6
                },
                "every_n_ticks": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "fewer_buttons": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "font_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "initial_position": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        20,
                        50,
                        500,
                        400
                    ]
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_axes_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_data_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_markers_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "c629bbfc-abed-4f59-a653-b12c8d61c28e"
        },
        "node5": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "b9f0bd20-20a6-4be3-adf2-0bccd08dd727"
        },
        "node6": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "correct": 0,
                        "incorrect": 1
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "0f8af791-c788-4a5b-b49b-1921ae867e79"
        },
        "node7": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "online_epoching": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "marker-locked"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        -10,
                        0
                    ]
                },
                "verbose": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "3201365f-ee8e-43f5-b9e8-fff5336d8532"
        },
        "node8": {
            "class": "InspectData",
            "module": "neuropype.nodes.visualization.InspectData",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_close": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 6
                },
                "every_n_ticks": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "fewer_buttons": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "font_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "initial_position": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        20,
                        50,
                        500,
                        400
                    ]
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_axes_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_data_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_markers_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "094e2f6f-c4d5-43ae-8ad5-5736298e30b1"
        },
        "node9": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "NER_2015_BCI_Challenge_Samples"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e00c40f6-e7f3-4d5c-80a1-93605c2ca84b"
        }
    },
    "version": 1.1
}</patch>
</scheme>
