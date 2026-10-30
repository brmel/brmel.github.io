{{- with .Get "q" }}[{{ $.Get "title" | default (i18n "map") }}](https://www.google.com/maps/search/?{{ querify "api" "1" "query" . }}){{ end -}}
