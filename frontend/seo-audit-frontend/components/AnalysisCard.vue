<template>
	<div class="bg-white p-4 rounded-lg shadow">
		<h3 class="text-lg font-semibold mb-2">{{ title }}</h3>
		<p :class="bad ? 'text-red-600' : 'text-gray-700'">
			{{ value }}
		</p>
	</div>
</template>

<script setup>
defineProps({
	title: String,
	value: [String, Number, Boolean],
	bad: {
		type: Boolean,
		default: false,
	},
});
</script>
