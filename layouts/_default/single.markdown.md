# {{ .Title }}

{{ with .Date }}{{ .Format "2006-01-02" }} · {{ end }}{{ .Permalink }}
{{ with .Description }}
> {{ . | plainify | htmlUnescape | chomp }}
{{ end }}
{{ .RenderShortcodes }}
