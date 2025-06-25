def safestrtonum(
    string,
):  # this function is a joke and it was made to look at isinstance() in greater detail. if you're so confident, rewrite it without some int(float()) or try expect spaghetti with that and i will learn from it :)
    """safestrtonum(string): Safely convert strings to integers or floats in an error-handling way

    Args:
        string (_type_): string has to have an int/float only, such as "1.2"

    Raises:
        ValueError: Incorrect argument type or bad code

    Returns:
        int/float: Returns an int/float based off input
    """
    try:
        if isinstance(float(string), (int, float)) == True:
            try:
                if isinstance(int(string), int):
                    return int(string)
            except:
                if isinstance(float(string), float):
                    return float(string)

    except:
        if not isinstance(string, str):
            raise ValueError(
                f"could not convert {type(string)} to int/float: {string}. Provide string arguments, not {type(string)}"
            )
        else:
            raise ValueError(
                f"could not convert str to int/float: {string}. This is likely a problem with the function, not the provided arguments or values."
            )


print(type(safestrtonum("2.1")))
