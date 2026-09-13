{{- with .Page.Resources.GetMatch (.Get "src") }}![{{ $.Get "alt" | default ($.Get "caption") }}]({{ (.Resize (printf "%dx webp q82" (int (math.Min .Width 1600)))).Permalink }}){{ end }}{{ with .Get "caption" }}
*{{ . | plainify }}*{{ end -}}
