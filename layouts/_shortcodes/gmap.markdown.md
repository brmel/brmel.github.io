{{- with .Get "q" }}[{{ $.Get "title" | default "Map" }}](https://www.google.com/maps/search/?{{ querify "api" "1" "query" . }}){{ end -}}
