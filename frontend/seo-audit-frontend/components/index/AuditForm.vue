<template>
	<form class="audit-form" @submit.prevent="onSubmit">
		<input
			:value="modelValue"
			@input="onInput"
			class="input"
			placeholder="https://example.com"
			autocomplete="url"
		/>
		<button class="btn" type="submit" :disabled="loading">
			{{ loading ? 'Scanning…' : 'Analyze' }}
		</button>
	</form>
</template>

<script setup>
const props = defineProps({
	modelValue: {
		type: String,
		default: '',
	},
	loading: {
		type: Boolean,
		default: false,
	},
});

const emit = defineEmits(['update:modelValue', 'submit']);

const onSubmit = () => emit('submit');
const onInput = (event) => emit('update:modelValue', event.target.value);
</script>

<style scoped>
.audit-form {
	display: flex;
	gap: 14px;
	margin-bottom: 30px;
}

@media (max-width: 640px) {
	.audit-form {
		flex-direction: column;
	}
}
</style>
