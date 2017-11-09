# 08-reactiveValues

library(shiny) #Libreria

ui <- fluidPage(
  actionButton(inputId = "norm", label = "Normal"),
  actionButton(inputId = "unif", label = "Uniform"),
  plotOutput("hist")
)

server <- function(input, output) {

  rv <- reactiveValues(data = rnorm(100)) #La grafica default

  observeEvent(input$norm, { rv$data <- rnorm(100) })
  #Cuando se aprete el boton Normal, se desplegaran 100 datos normales
  observeEvent(input$unif, { rv$data <- runif(100) })
  #Cuando se active el boton Uniforme, se desplegaran 100 datos uniformes

  output$hist <- renderPlot({ 
    hist(rv$data) 
    #Los datos generados se mostraran en un histograma
  })
}

shinyApp(ui = ui, server = server)
