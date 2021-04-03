<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEBME6099FinalProject" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(44.0, 467.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="67fc899b-315d-480c-aa62-c61bf45bdfb9" version="1.0.0" />
		<node id="1" name="Spectrum Plot" position="(439.0, 325.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" title="Spectrum Plot" uuid="6a8de5a7-368f-4457-9cca-96e942412c63" version="1.0.0" />
		<node id="2" name="Power Spectrum (Welch)" position="(278.0, 261.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owwelchspectrum.OWWelchSpectrum" title="Power Spectrum (Welch)" uuid="e9e2e609-9f39-47e6-ae80-dddac9353d15" version="1.0.0" />
		<node id="3" name="Inspect Data" position="(431.0, 218.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data (1)" uuid="3ff6f4f1-d29a-4ebd-8244-16b098750dac" version="2.1.1" />
		<node id="4" name="Dejitter Timestamps" position="(166.0, 485.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="e4fea98d-4337-45c2-a285-51ee4ce304e6" version="1.0.0" />
		<node id="5" name="Assign Target Values" position="(277.0, 459.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Target Values" uuid="e0e25250-55b5-43f5-b5f3-59f3298028ed" version="1.0.0" />
		<node id="6" name="Segmentation" position="(394.0, 469.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="f99a6fc2-6ed2-4041-add1-b20d4a7d00f6" version="1.0.1" />
		<node id="7" name="Hierarchical Discriminant Component Analysis" position="(643.0, 457.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owhierarchicaldiscriminantcomponentanalysis.OWHierarchicalDiscriminantComponentAnalysis" title="Hierarchical Discriminant Component Analysis" uuid="2c466609-06e9-4cfc-9958-c693534c4d13" version="1.0.0" />
		<node id="8" name="Select Range" position="(742.0, 514.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="70a48cf5-2e7c-486a-892f-0440fe850704" version="1.0.0" />
		<node id="9" name="Override Axis" position="(771.0, 402.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="667598f1-9579-431f-9335-250556fda846" version="1.0.2" />
		<node id="10" name="Time Series Plot" position="(862.0, 566.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="a2a336a4-a9a7-4d52-bd1b-4a15f9e2bf2f" version="1.0.1" />
		<node id="11" name="Streaming Bar Plot" position="(910.0, 372.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="650b32af-ce02-4ad5-a4c0-530359b78684" version="1.0.2" />
		<node id="12" name="Inspect Data" position="(492.0, 597.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data (2)" uuid="e6a34b13-0db4-40b2-a992-8bebcc2ef37e" version="2.1.1" />
		<node id="13" name="LSL Output" position="(537.0, 397.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="df4025cf-911a-4894-867b-bdb04830003e" version="1.0.0" />
		<node id="14" name="LSL Output" position="(210.0, 649.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output (1)" uuid="3d0b8ecd-0ca0-464a-8dd9-cff063224151" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="0" />
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
WAMAAABQTzdxNlgDAAAAUE96cTdYAwAAAFAwOHE4WAIAAABPMXE5WAIAAABPMnE6ZVgLAAAAZGlh
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
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABjbGFzc193ZWlnaHRzcQFYDQAAACh1c2UgZGVmYXVsdClxAlgQAAAAZG9udF9y
ZXNldF9tb2RlbHEDiVgPAAAAaW5pdGlhbGl6ZV9vbmNlcQSIWA0AAABwcm9iYWJpbGlzdGljcQWI
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0
NC5RdENvcmVxCFgKAAAAUUJ5dGVBcnJheXEJQy4B2dDLAAEAAAAABNYAAAKcAAAGyQAAA5wAAATe
AAACuwAABsEAAAOUAAAAAAAAcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWBAAAABz
aHJpbmthZ2VfYWNyb3NzcQ9HP7HrhR64UexYEAAAAHNocmlua2FnZV93aXRoaW5xEEc/qZmZmZmZ
mlgJAAAAdG9sZXJhbmNlcRFHPxo24uscQy1YBwAAAHZlcmJvc2VxEol1Lg==
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVx
A1gTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlR
dDQuUXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAASzAAACaAAABioAAAMzAAAE
uwAAAocAAAYiAAADKwAAAAAAAHEIhXEJh3EKUnELWAkAAABzZWxlY3Rpb25xDF1xDUsBYVgOAAAA
c2V0X2JyZWFrcG9pbnRxDolYBAAAAHVuaXRxD1gHAAAAaW5kaWNlc3EQdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4lYDAAAAGN1c3RvbV9sYWJlbHEEWA0AAAAodXNlIGRlZmF1
bHQpcQVYCQAAAGluaXRfZGF0YXEGXXEHKFgHAAAAY29ycmVjdHEIWAkAAABpbmNvcnJlY3RxCWVY
CAAAAG5ld19heGlzcQpYBwAAAGZlYXR1cmVxC1gIAAAAb2xkX2F4aXNxDFgHAAAAZmVhdHVyZXEN
WAwAAABvbmx5X3NpZ25hbHNxDohYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxD2NzaXAKX3VucGlj
a2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0Q29yZXERWAoAAABRQnl0ZUFycmF5cRJDLgHZ0MsAAQAA
AAAEcgAAAkgAAAXpAAADQAAABHoAAAJnAAAF4QAAAzgAAAAAAABxE4VxFIdxFVJxFlgOAAAAc2V0
X2JyZWFrcG9pbnRxF4l1Lg==
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWJWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksy
TbwCTfQBZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKJWA4AAABub19jb25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReJWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAAAABHIAAAH9AAAF6QAAA4sAAAR6AAACHAAABeEA
AAODAAAAAAAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP/AAAAAAAABYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIolYCwAAAHN0cmVhbV9uYW1lcSNoFVgKAAAAdGltZV9y
YW5nZXEkSwpYBQAAAHRpdGxlcSVYIwAAAFByb2JhYmlsaXR5IG9mIHVzZXIgZXJyb3Igb3ZlciB0
aW1lcSZYCgAAAHplcm9fY29sb3JxJ1gHAAAAIzdGN0Y3RnEoWAgAAAB6ZXJvbWVhbnEpiXUu
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVxA1gQAAAA
YmFja2dyb3VuZF9jb2xvcnEEWAcAAAAjRkZGRkZGcQVYCQAAAGJhcl9jb2xvcnEGWAEAAABicQdY
CQAAAGJhcl93aWR0aHEIRz/szMzMzMzNWAwAAABpbml0aWFsX2RpbXNxCV1xCihLMksyTbwCTfQB
ZVgOAAAAaW5zdGFuY2VfZmllbGRxC1gNAAAAKHVzZSBkZWZhdWx0KXEMWA4AAABsYWJlbF9yb3Rh
dGlvbnENWAoAAABob3Jpem9udGFscQ5YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxD2NzaXAKX3Vu
cGlja2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0Q29yZXERWAoAAABRQnl0ZUFycmF5cRJDLgHZ0MsA
AQAAAAAFwQAAAfAAAAc4AAADRQAABckAAAIPAAAHMAAAAz0AAAAAAABxE4VxFIdxFVJxFlgOAAAA
c2V0X2JyZWFrcG9pbnRxF4lYDAAAAHNob3dfdG9vbGJhcnEYiVgLAAAAc3RyZWFtX25hbWVxGWgM
WAUAAAB0aXRsZXEaWBUAAABDbGFzc2lmaWNhdGlvbiBPdXRwdXRxG1gRAAAAdXNlX2xhc3RfaW5z
dGFuY2VxHIhYBwAAAHZlcmJvc2VxHYlYCAAAAHlfbGltaXRzcR5dcR8oSwBLAWV1Lg==
</properties>
		<properties format="literal" node_id="12">{'always_on_top': True, 'auto_close': False, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': True, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAABS4AAALQAAAGpQAA
BE8AAAU2AAAC7wAABp0AAARHAAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETaAZYBQAAAHNyYXRlcRRYDQAAACh1
c2UgZGVmYXVsdClxFVgLAAAAc3RyZWFtX25hbWVxFlgeAAAATkVSXzIwMTVfQkNJX0NoYWxsZW5n
ZV9TYW1wbGVzcRdYCwAAAHN0cmVhbV90eXBlcRhYBwAAAENvbnRyb2xxGVgTAAAAdXNlX2RhdGFf
dGltZXN0YW1wc3EaiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEbiXUu
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAABHIAAAIFAAAF6QAA
A4QAAAR6AAACJAAABeEAAAN8AAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETaAZYBQAAAHNyYXRlcRRYDQAAACh1
c2UgZGVmYXVsdClxFVgLAAAAc3RyZWFtX25hbWVxFlgMAAAAUHlwZUluQW5kT3V0cRdYCwAAAHN0
cmVhbV90eXBlcRhYBwAAAENvbnRyb2xxGVgTAAAAdXNlX2RhdGFfdGltZXN0YW1wc3EaiFgWAAAA
dXNlX251bXB5X29wdGltaXphdGlvbnEbiXUu
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
            "node15",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data"
        ],
        [
            "node6",
            "data",
            "node7",
            "data"
        ],
        [
            "node9",
            "data",
            "node11",
            "data"
        ],
        [
            "node10",
            "data",
            "node12",
            "data"
        ],
        [
            "node7",
            "data",
            "node14",
            "data"
        ],
        [
            "node7",
            "data",
            "node13",
            "data"
        ],
        [
            "node7",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node10",
            "data"
        ],
        [
            "node8",
            "data",
            "node9",
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
                        "P08",
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
            "uuid": "67fc899b-315d-480c-aa62-c61bf45bdfb9"
        },
        "node10": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "correct",
                        "incorrect"
                    ]
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "667598f1-9579-431f-9335-250556fda846"
        },
        "node11": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
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
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
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
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
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
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 10
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Probability of user error over time"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a2a336a4-a9a7-4d52-bd1b-4a15f9e2bf2f"
        },
        "node12": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.9
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
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "horizontal"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Classification Output"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "650b32af-ce02-4ad5-a4c0-530359b78684"
        },
        "node13": {
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
            "uuid": "e6a34b13-0db4-40b2-a992-8bebcc2ef37e"
        },
        "node14": {
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
            "uuid": "df4025cf-911a-4894-867b-bdb04830003e"
        },
        "node15": {
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
                    "value": "PypeInAndOut"
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
            "uuid": "3d0b8ecd-0ca0-464a-8dd9-cff063224151"
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
            "uuid": "6a8de5a7-368f-4457-9cca-96e942412c63"
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
            "uuid": "e9e2e609-9f39-47e6-ae80-dddac9353d15"
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
                    "customized": false,
                    "type": "IntPort",
                    "value": 50
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "3ff6f4f1-d29a-4ebd-8244-16b098750dac"
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
            "uuid": "e4fea98d-4337-45c2-a285-51ee4ce304e6"
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
            "uuid": "e0e25250-55b5-43f5-b5f3-59f3298028ed"
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
            "uuid": "f99a6fc2-6ed2-4041-add1-b20d4a7d00f6"
        },
        "node8": {
            "class": "HierarchicalDiscriminantComponentAnalysis",
            "module": "neuropype.nodes.machine_learning.HierarchicalDiscriminantComponentAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initialize_once": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage_across": {
                    "customized": true,
                    "type": "Port",
                    "value": 0.07
                },
                "shrinkage_within": {
                    "customized": true,
                    "type": "Port",
                    "value": 0.05
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "2c466609-06e9-4cfc-9958-c693534c4d13"
        },
        "node9": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        1
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "70a48cf5-2e7c-486a-892f-0440fe850704"
        }
    },
    "version": 1.1
}</patch>
</scheme>
