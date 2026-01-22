from fastmcp import FastMCP
from typing import Annotated

mcp = FastMCP("CalculatorServer")

@mcp.tool(
    name="price after increase",
    description="Calculate the price after an increase, 'a' represents the original price and 'b' represents the rate of increase.",
    annotations={"title": "Calculate rise"}
)
def price_after_increase(a: Annotated[float, "The original price"], b: Annotated[float, "The rate of increase"]) -> float:
    return a + a * b

@mcp.tool(
    name="price after decrease",
    description="Calculate the price after the decrease, 'a' represents the original price and 'b' represents the rate of decrease.",
    annotations={"title": "Calculate fall"}
)
def price_after_decrease(a: Annotated[float, "The original price"], b: Annotated[float, "The rate of decrease"]) -> float:
    return a - a * b

if __name__ == "__main__":
    mcp.run()