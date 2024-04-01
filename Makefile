SHELL := /bin/zsh


PYTHON_SERVICES := python-service-one
DOTNET_SERVICES := dotnet-service-one

OUT_DIR := generated

.PHONY: npm-install all clean $(PYTHON_SERVICES) $(DOTNET_SERVICES)

python: $(PYTHON_SERVICES)
dotnet: $(DOTNET_SERVICES)
all: python dotnet

$(PYTHON_SERVICES):
	@echo "Generating Python code for $@..."
	protoc --proto_path=service/$@ --python_out=$(OUT_DIR) service/$@/*.proto
	@echo "Python code generated successfully for $@."
$(DOTNET_SERVICES):
	@echo "Generating C# code for $@..."
	protoc --proto_path=service/$@ --csharp_out=$(OUT_DIR) service/$@/*.proto
	@echo "C# code generated successfully for $@."

clean:
	@echo "Cleaning generated files..."
	rm -rf $(OUT_DIR)/*.*
	@echo "Cleanup completed."
npm-install:
	source ~/.nvm/nvm.sh && nvm use && npm install
