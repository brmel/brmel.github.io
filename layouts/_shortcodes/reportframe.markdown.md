{{- with resources.Get (.Get "src") }}[{{ $.Get "title" | default "Report" }}]({{ .Permalink }}){{ end -}}
