{{- with .Get "id" | default (.Get 0) }}[YouTube video](https://www.youtube.com/watch?v={{ . }}){{ end -}}
