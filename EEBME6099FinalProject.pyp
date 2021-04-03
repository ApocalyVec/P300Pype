<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEBME6099FinalProject" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(32.0, 78.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="353bffc0-2c17-4d37-8d0e-7d86ad87f06e" version="1.0.0" />
		<node id="1" name="Spectrum Plot" position="(427.0, -64.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" title="Spectrum Plot" uuid="e3924c6e-4887-451b-be0a-310ed3aca75d" version="1.0.0" />
		<node id="2" name="Power Spectrum (Welch)" position="(266.0, -128.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owwelchspectrum.OWWelchSpectrum" title="Power Spectrum (Welch)" uuid="2ca5ac93-950d-4f25-b9aa-837739a4c100" version="1.0.0" />
		<node id="3" name="Inspect Data" position="(419.0, -171.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data (1)" uuid="8a232a4a-04aa-468a-a6ec-3dd9bc060957" version="2.1.1" />
		<node id="4" name="Dejitter Timestamps" position="(158.0, 71.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="8ac0c798-a8dc-44f9-8dab-9f24a9008f8f" version="1.0.0" />
		<node id="5" name="Assign Target Values" position="(265.0, 71.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Target Values" uuid="6e3a2a3f-0768-4e71-b931-cb7423af402a" version="1.0.0" />
		<node id="6" name="Segmentation" position="(382.0, 80.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="452d9e05-484c-46c1-b6b1-45bd098a4881" version="1.0.1" />
		<node id="7" name="FFT Band-Pass Filter" position="(480.0, 82.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owspectralselection.OWSpectralSelection" title="FFT Band-Pass Filter" uuid="84db8ea1-b8cc-4949-9138-2c419f0a9994" version="1.0.0" />
		<node id="8" name="Hierarchical Discriminant Component Analysis" position="(597.0, 87.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owhierarchicaldiscriminantcomponentanalysis.OWHierarchicalDiscriminantComponentAnalysis" title="Hierarchical Discriminant Component Analysis" uuid="7d486bda-8ffd-4177-99d8-ea38b73939df" version="1.0.0" />
		<node id="9" name="Discard Long Chunks" position="(714.0, 92.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdiscardlongchunks.OWDiscardLongChunks" title="Discard Long Chunks" uuid="510c2bae-864c-4599-bbaf-e2e7e692c3f5" version="1.0.0" />
		<node id="10" name="Select Range" position="(803.0, 88.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="827f91c8-d14b-40fa-a6fe-def020855615" version="1.0.0" />
		<node id="11" name="Override Axis" position="(847.0, 230.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="068a0e0b-48b2-4656-b0ca-fd2510dba17e" version="1.0.2" />
		<node id="12" name="Time Series Plot" position="(860.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="248d34f2-c30f-46f2-a8ba-fc4c0cdb6bfa" version="1.0.1" />
		<node id="13" name="Inspect Data" position="(213.0, 291.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data" uuid="407fc261-e7dd-4fc7-99d5-c1c7287e1cc1" version="2.1.1" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="11" />
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
LlF0Q29yZXENWAoAAABRQnl0ZUFycmF5cQ5DLgHZ0MsAAQAAAAAEWgAAAngAAAXRAAADKwAABGIA
AAKXAAAFyQAAAyMAAAAAAABxD4VxEIdxEVJxElgOAAAAc2V0X2JyZWFrcG9pbnRxE4lYEQAAAHN1
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
		<properties format="pickle" node_id="7">gAN9cQAoWAkAAABibG9ja3NpemVxAUtkWAsAAABmcmVxdWVuY2llc3ECXXEDKEc/uZmZmZmZmksP
ZVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlR
dDQuUXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAARyAAACgQAABekAAAMHAAAE
egAAAqAAAAXhAAAC/wAAAAAAAHEIhXEJh3EKUnELWA4AAABzZXRfYnJlYWtwb2ludHEMiXUu
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABjbGFzc193ZWlnaHRzcQFYDQAAACh1c2UgZGVmYXVsdClxAlgQAAAAZG9udF9y
ZXNldF9tb2RlbHEDiVgPAAAAaW5pdGlhbGl6ZV9vbmNlcQSIWA0AAABwcm9iYWJpbGlzdGljcQWI
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0
NC5RdENvcmVxCFgKAAAAUUJ5dGVBcnJheXEJQy4B2dDLAAEAAAAABHIAAAJWAAAGZQAAA1YAAAR6
AAACdQAABl0AAANOAAAAAAAAcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWBAAAABz
aHJpbmthZ2VfYWNyb3NzcQ9HP7HrhR64UexYEAAAAHNocmlua2FnZV93aXRoaW5xEEc/qZmZmZmZ
mlgJAAAAdG9sZXJhbmNlcRFHPxo24uscQy1YBwAAAHZlcmJvc2VxEol1Lg==
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA0AAABlbnRpcmVfcGFja2V0cQGIWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQJjc2lw
Cl91bnBpY2tsZV90eXBlCnEDWAwAAABQeVF0NC5RdENvcmVxBFgKAAAAUUJ5dGVBcnJheXEFQy4B
2dDLAAEAAAAABHIAAAJ3AAAF6QAAAxIAAAR6AAAClgAABeEAAAMKAAAAAAAAcQaFcQeHcQhScQlY
DgAAAHNldF9icmVha3BvaW50cQqJWAkAAAB0aHJlc2hvbGRxC0sPdS4=
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVx
A1gTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlR
dDQuUXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAARyAAACXwAABekAAAMqAAAE
egAAAn4AAAXhAAADIgAAAAAAAHEIhXEJh3EKUnELWAkAAABzZWxlY3Rpb25xDF1xDUsBYVgOAAAA
c2V0X2JyZWFrcG9pbnRxDolYBAAAAHVuaXRxD1gHAAAAaW5kaWNlc3EQdS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4lYDAAAAGN1c3RvbV9sYWJlbHEEWA0AAAAodXNlIGRlZmF1
bHQpcQVYCQAAAGluaXRfZGF0YXEGXXEHWAgAAABQKGVycm9yKXEIYVgIAAAAbmV3X2F4aXNxCVgH
AAAAZmVhdHVyZXEKWAgAAABvbGRfYXhpc3ELWAcAAABmZWF0dXJlcQxYDAAAAG9ubHlfc2lnbmFs
c3ENiFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEOY3NpcApfdW5waWNrbGVfdHlwZQpxD1gMAAAA
UHlRdDQuUXRDb3JlcRBYCgAAAFFCeXRlQXJyYXlxEUMuAdnQywABAAAAAARyAAACSAAABekAAANA
AAAEegAAAmcAAAXhAAADOAAAAAAAAHEShXETh3EUUnEVWA4AAABzZXRfYnJlYWtwb2ludHEWiXUu
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
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
		<properties format="pickle" node_id="13">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGIWAoAAABhdXRvX2Nsb3NlcQKJWAgAAABjb2xfYXhp
c3EDWAQAAAB0aW1lcQRYCAAAAGRlY2ltYWxzcQVLBlgNAAAAZXZlcnlfbl90aWNrc3EGSwFYDQAA
AGZld2VyX2J1dHRvbnNxB4hYCQAAAGZvbnRfc2l6ZXEISwpYEAAAAGluaXRpYWxfcG9zaXRpb25x
CV1xCihLFEsyTfQBTZABZVgIAAAAcm93X2F4aXNxC1gFAAAAc3BhY2VxDFgTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXENY3NpcApfdW5waWNrbGVfdHlwZQpxDlgMAAAAUHlRdDQuUXRDb3JlcQ9YCgAA
AFFCeXRlQXJyYXlxEEMuAdnQywABAAAAAAauAAABmgAACCUAAAMBAAAGtgAAAbkAAAgdAAAC+QAA
AAAAAHERhXESh3ETUnEUWA4AAABzZXRfYnJlYWtwb2ludHEViVgPAAAAc2hvd19heGVzX3RhYmxl
cRaIWA8AAABzaG93X2RhdGFfdGFibGVxF4hYEgAAAHNob3dfbWFya2Vyc190YWJsZXEYiFgQAAAA
c2hvd19tYXhfY29sdW1uc3EZSxRYDwAAAHNob3dfbWF4X3ZhbHVlc3EaSzJYEgAAAHNob3dfc3Ry
ZWFtc190YWJsZXEbiFgLAAAAc3RyZWFtX25hbWVxHFgDAAAAZWVncR1YDAAAAHdpbmRvd190aXRs
ZXEeWBMAAABJbnNwZWN0IERhdGEgUGFja2V0cR91Lg==
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
            "node1",
            "data",
            "node5",
            "data"
        ],
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
            "node7",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node9",
            "data"
        ],
        [
            "node9",
            "data",
            "node10",
            "data"
        ],
        [
            "node10",
            "data",
            "node11",
            "data"
        ],
        [
            "node11",
            "data",
            "node12",
            "data"
        ],
        [
            "node12",
            "data",
            "node13",
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
            "uuid": "353bffc0-2c17-4d37-8d0e-7d86ad87f06e"
        },
        "node10": {
            "class": "DiscardLongChunks",
            "module": "neuropype.nodes.utilities.DiscardLongChunks",
            "params": {
                "entire_packet": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "threshold": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 15
                }
            },
            "uuid": "510c2bae-864c-4599-bbaf-e2e7e692c3f5"
        },
        "node11": {
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
            "uuid": "827f91c8-d14b-40fa-a6fe-def020855615"
        },
        "node12": {
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
                        "P(error)"
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
            "uuid": "068a0e0b-48b2-4656-b0ca-fd2510dba17e"
        },
        "node13": {
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
            "uuid": "248d34f2-c30f-46f2-a8ba-fc4c0cdb6bfa"
        },
        "node14": {
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
            "uuid": "407fc261-e7dd-4fc7-99d5-c1c7287e1cc1"
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
            "uuid": "e3924c6e-4887-451b-be0a-310ed3aca75d"
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
            "uuid": "2ca5ac93-950d-4f25-b9aa-837739a4c100"
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
            "uuid": "8a232a4a-04aa-468a-a6ec-3dd9bc060957"
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
            "uuid": "8ac0c798-a8dc-44f9-8dab-9f24a9008f8f"
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
            "uuid": "6e3a2a3f-0768-4e71-b931-cb7423af402a"
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
            "uuid": "452d9e05-484c-46c1-b6b1-45bd098a4881"
        },
        "node8": {
            "class": "SpectralSelection",
            "module": "neuropype.nodes.spectral.SpectralSelection",
            "params": {
                "blocksize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        15
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "84db8ea1-b8cc-4949-9138-2c419f0a9994"
        },
        "node9": {
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
            "uuid": "7d486bda-8ffd-4177-99d8-ea38b73939df"
        }
    },
    "version": 1.1
}</patch>
</scheme>
