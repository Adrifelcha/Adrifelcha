library(shiny)  


ui <- fluidPage("Adriana F Chavez - Lab25",
                sliderInput(inputId="num", 
                            label = "Choose a number",
                            value=25, min=1, max=100),
                textInput(inputId = "titulo",
                          label = "Titulo", 
                          value = "Histograma"),
                textInput(inputId = "evidence",
                          label = "Datos", 
                          value = "Variable"),
                actionButton(inputId="click", label ="Click me!"),
                actionButton(inputId="go", label ="Update Graph"),
                plotOutput(outputId="hist"),
                verbatimTextOutput("stats"))

server <- function(input, output) {
  data <- eventReactive(input$go, {rnorm(input$num)})
  output$hist <- renderPlot({hist(data(), xlab=input$evidence, 
                                  ylab='Slider', main=input$titulo)})
  output$stats <- renderPrint({summary(data())})
  observeEvent(input$click, {print(as.numeric(input$click))})
}

shinyApp(ui = ui, server = server)