# Consulta à API de dados meteorológicos
library(httr)
library(jsonlite)

cidade <- "Conceição da Aparecida - MG"

latitude <- -21.0946
longitude <- -46.2030

url <- paste0(
  "https://api.open-meteo.com/v1/forecast?latitude=",
  latitude,
  "&longitude=",
  longitude,
  "&current_weather=true"
)

response <- GET(url)

if (status_code(response) == 200) {

  dados <- fromJSON(content(response, "text"))

  temperatura <- dados$current_weather$temperature
  vento <- dados$current_weather$windspeed
  horario <- dados$current_weather$time

  cat("Cidade:", cidade, "\n")
  cat("Horário:", horario, "\n")
  cat("Temperatura:", temperatura, "°C\n")
  cat("Velocidade do vento:", vento, "km/h\n")

} else {
  cat("Erro ao acessar API\n")
}