# {{ .Title }}

{{ with .Date }}{{ .Format "2006-01-02" }} · {{ end }}{{ .Permalink }}
{{ with .Description }}
> {{ . | plainify | htmlUnescape | chomp }}
{{ end }}
{{ .RenderShortcodes }}
{{- with .Params.findings }}

## {{ i18n "report_findings" }}
{{ range . }}
- {{ . }}
{{- end }}
{{- end }}
{{- with .Params.methods }}

## {{ i18n "report_methods" }}

{{ . }}
{{- end }}
