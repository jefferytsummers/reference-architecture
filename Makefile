SHELL := /bin/zsh


SERVICE_NAMES := python-service-one python-service-two python-service-three
OUT_DIR := generated

.PHONY: npm-install all clean $(SERVICE_NAMES)

all: $(SERVICE_NAMES)

$(SERVICE_NAMES):
	@echo "Generating Python code for $@..."
	protoc --proto_path=service/$@ --python_out=$(OUT_DIR) service/$@/*.proto
	@echo "Python code generated successfully for $@."

clean:
	@echo "Cleaning generated files..."
	rm -rf $(PROTO_DIR)/*/$(OUT_DIR)/*.py
	@echo "Cleanup completed."
npm-install:
	source ~/.nvm/nvm.sh && nvm use && npm install

generate-dotnet:
	protoc --csharp_out=./dotnet_generated_proto --csharp_opt=base_namespace=GeneratedProtobuf ./proto/commands.proto

generate-python-contracts:
	echo  "$(CONTRACT_DIR)"
	python3 -m grpc_tools.protoc -I. --python_out=./command_queue/src/commands/proto/ --grpc_python_out=./command_queue/src/commands/proto/ ./service/$(CONTRACT_DIR)/entity.proto


test:
	@for contract in $(PYTHON_CONTRACTS); do \
		/usr/bin/make generate-python-contracts CONTRACT_DIR=$(contract); \
	done

