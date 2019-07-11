.PHONY: avaza
avaza: swagger.json
	docker run --user $(shell id -u ${USER}):$(shell id -g ${USER}) --rm \
		-v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
		--lang python \
		--input-spec ./local/swagger.json \
		--config ./local/swagger-config.json \
		--output ./local

		# https://github.com/swagger-api/swagger-codegen/issues/8328
		find . -name '*.py' -exec sed -i 's/async=params.get/is_async=params.get/g' {} +
		find . -name '*.py' -exec sed -i 's/async=None/is_async=None/g' {} +
		find . -name '*.py' -exec sed -i 's/if not async/if not is_async/g' {} +


swagger.json:
	curl -s https://api.avaza.com/swagger/docs/v1 | jq -r '.' > swagger.json
