<p align="center"><a href="https://github.com/anuraghazra/github-readme-stats">
  <img align="center" src="https://github-readme-stats.vercel.app/api?username=r3mcos3&show_icons=true&theme=tokyonight" />
</a></p>

<p align="center"><a href="https://wakatime.com/@r3mcos3">
  <img align="center" width="400" height="300" src="https://wakatime.com/share/@r3mcos3/3e8eabe0-6dab-4358-826f-46c28cdeea19.svg"/>
</a>
<a href="https://wakatime.com/@r3mcos3">
  <img align="center" width="400" height="300" src="https://wakatime.com/share/@r3mcos3/c6d0e7bb-c9fe-48c7-8bf2-a66fee960e05.svg" />
</a></p>

<p align="center"><a href="https://wakatime.com/@r3mcos3">
  <img align="center" width="400" height="300" src="https://wakatime.com/share/@r3mcos3/aad91693-62d4-4a25-a498-12b4ab75a904.svg" />
</a>
<a href="https://wakatime.com/@r3mcos3">
  <img align="center" width="400" height="300" src="https://wakatime.com/share/@r3mcos3/53d8d942-5fd4-41e9-a426-72deb45ce0a0.svg" />
</a></p>

### 👷 Check out what I'm currently working on
{{ range recentContributions 5 }}
- [{{ .Repo.Name }}]({{ .Repo.URL }}) - {{ .Repo.Description }}
{{- end }}
### 🌱 My latest projects
{{ range recentRepos 5 }}
- [{{ .Name }}]({{ .URL }}) - {{ .Description }}
{{- end }}
### 🔨 My recent Pull Requests
{{ range recentPullRequests 5 }}
- [{{ .Title }}]({{ .URL }}) on [{{ .Repo.Name }}]({{ .Repo.URL }})
{{- end }}
### ⭐ Recent Stars
{{ range recentStars 5 }}
- [{{ .Repo.Name }}]({{ .Repo.URL }}) - {{ .Repo.Description }}
{{- end }}
 
