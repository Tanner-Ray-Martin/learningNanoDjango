Here’s an updated `README.md` that uses `pixi` for setup, installation, and running instructions:

```markdown
# learningNanoDjango

A simple project to explore [NanoDjango](https://github.com/radiac/nanodjango) with example applications, including `counter` and `hello_async`. These examples are taken from the NanoDjango repository to help understand and run basic asynchronous Django-style apps.

## Project Setup

### Requirements

- **Python**: >= 3.13, < 3.14
- **NanoDjango**: >= 0.9.2, < 0.10
- **Conda**: uses the `conda-forge` channel

### Installation and Setup with Pixi

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd learningNanoDjango
   ```

2. Use `pixi` to create the environment, install dependencies, and set up the project:
   ```bash
   pixi install
   ```

This command will handle environment creation, dependency installation, and make `learningNanoDjango` editable in your environment.

## Running Examples

This project includes two examples from the NanoDjango repository: `counter` and `hello_async`. Each example can be run through `pixi` as follows:

### Running the Counter Example

Run the `counter` example using `pixi`:
```bash
pixi run counter
```

Then, open your browser and go to `http://127.0.0.1:8000` to see the counter application in action.

### Running the Hello Async Example

To run the `hello_async` example:
```bash
pixi run hello
```

Open your browser at `http://127.0.0.1:8000` to interact with the application.

## Project Details

- **Author**: Tanner Ray Martin ([tanner.ray.martin.123@gmail.com](mailto:tanner.ray.martin.123@gmail.com))
- **Project Version**: 0.1.0
- **Python Requirement**: 3.13.x
- **Build System**: Hatchling

## Development

To develop and test further with NanoDjango examples or create new examples, add scripts and follow similar structures as the provided examples in the `src/learningnanodjango` folder. Use `pixi` for running, testing, and managing dependencies.

## License

This project is intended for educational purposes and does not currently include a specific license.
```

This version relies entirely on `pixi` for setup, installation, and execution of tasks, streamlining the process for anyone setting up the project. Let me know if there's anything else you'd like added!