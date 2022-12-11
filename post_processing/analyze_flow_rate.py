import regex as re


DATA_PATH = "./post_processing/data/"

def pop_whitespace(content: list[str]) -> str:
    """Removes any whitespace lines from a list of strings. Modifies in place and returns."""
    while content[0].isspace():
        content.pop(0)
    
    return content


class LoadCellOutput:

    def __init__(self, content: str) -> None:
        lines = content.splitlines()

        # Remove calibration header and load calibration values
        del lines[0]
        self.calibration1 = float(lines.pop(0))
        self.calibration2 = float(lines.pop(0))
        self.calibration3 = float(lines.pop(0))

        lines = pop_whitespace(lines)
        
        

        

def split_file_by_runs(path: str):
    """Reads the .txt located and path and finds all of the separate times the device was started and stopped. It splits each one into a separate file located in the data folder."""

    with open(path, "r") as f:
        contents = f.read()

        contents = contents.split("cals")

        for content in contents:
            create_file_from_content("cals" + content)




if __name__ == "__main__":
    split_file_by_runs(DATA_PATH + "durability_test.txt")