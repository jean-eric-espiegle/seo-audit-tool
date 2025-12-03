<template>
	<div class="bg-white p-6 rounded-xl shadow">
		<h3 class="text-lg font-semibold mb-2">{{ title }}</h3>
		<p :class="valueClass">
			{{ displayValue }}
		</p>
	</div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
	title: {
		type: String,
		required: true,
	},
	value: {
		type: [String, Number, Boolean, Object, null],
		default: null,
	},
	bad: {
		type: Boolean,
		default: false,
	},
});

const valueClass = computed(() =>
	props.bad ? 'text-red-600 font-semibold' : 'text-gray-800',
);

const displayValue = computed(() => {
	const v = props.value;
	if (v === true) return 'Yes';
	if (v === false) return 'No';
	if (v === null || v === undefined || v === '') return 'Not found';
	return v;
});
</script>
