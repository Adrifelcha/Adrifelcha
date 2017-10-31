library(shiny)

ui <- fluidPage("Adriana F Chavez - Lab25",
                sliderInput(inputId="num", 
                            label = "Choose a number",
                            value=25, min=1, max=100),
                plotOutput(outputId="hist"))

server <- function(input, output) {
  output$hist <- renderPlot({barplot(input$num, xlim=c(0,1.5), ylim=c(0,100), main = "Just a simple set of graphs", 
                                     xlab='Variable', ylab='Slider')})
}

shinyApp(ui = ui, server = server)