import sys

from handheld_device import HandheldDevice
import p1


def get_answer(input_text: str):
    """Return the image drawn on the device's screen after the program is run."""
    device = HandheldDevice()
    instructions = p1.get_instructions(input_text)
    instruction = next(instructions)
    while True:
        device.draw_current_pixel_if_needed()
        instruction_opcode, parameters = instruction
        device.run(instruction_opcode, parameters)
        if device.is_ready_for_next:
            try:
                instruction = next(instructions)
            except StopIteration:
                break

    return device.render_screen()


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
