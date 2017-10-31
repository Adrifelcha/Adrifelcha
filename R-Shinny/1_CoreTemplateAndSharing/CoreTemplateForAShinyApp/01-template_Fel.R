library(shiny)

ui <- fluidPage("Adriana F Chavez - Lab25",
                sliderInput(inputId="num", 
                            label = "Choose a number",
                            value=25, min=1, max=100),
                plotOutput(outputId="hist"))

server <- function(input, output) {
  output$hist <- renderPlot({hist(rnorm(input$num), main = "Just another Histogram")})
}

shinyApp(ui = ui, server = server)