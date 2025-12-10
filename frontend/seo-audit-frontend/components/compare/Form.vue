<template>
	<form class="compare-form card" @submit.prevent="onSubmit">
		<div class="form-row">
			<div class="field">
				<label for="url1">First URL</label>
				<input
					id="url1"
					:value="url1"
					@input="onInput('url1', $event)"
					type="text"
					class="input"
					placeholder="https://example.com"
					required
				/>
			</div>

			<div class="field">
				<label for="url2">Second URL</label>
				<input
					id="url2"
					:value="url2"
					@input="onInput('url2', $event)"
					type="text"
					class="input"
					placeholder="https://competitor.com"
					required
				/>
			</div>

			<div class="field action-field">
				<label>&nbsp;</label>
				<button class="btn" type="submit" :disabled="loading">
					{{ loading ? 'Comparing…' : 'Compare' }}
				</button>
			</div>
		</div>
	</form>
</template>

<script setup>
const props = defineProps({
	url1: {
		type: String,
		default: '',
	},
	url2: {
		type: String,
		default: '',
	},
	loading: {
		type: Boolean,
		default: false,
	},
});

const emit = defineEmits(['update:url1', 'update:url2', 'submit']);

const onSubmit = () => emit('submit');
const onInput = (key, event) => emit(`update:${key}`, event.target.value);
</script>

<style scoped>
.compare-form {
	margin-bottom: 20px;
}

.form-row {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
	gap: 16px;
	align-items: end;
}

.field {
	display: flex;
	flex-direction: column;
	gap: 6px;
}

@media (max-width: 720px) {
	.compare-form {
		margin-bottom: 16px;
	}
}
</style>
