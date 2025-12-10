<template>
	<div
		class="card score-card"
		v-if="seoScore !== null && seoScore !== undefined"
	>
		<h2 class="card-title">SEO Score</h2>

		<div class="score-wrapper">
			<svg width="170" height="170">
				<circle
					cx="85"
					cy="85"
					r="70"
					stroke="#e5e7eb"
					stroke-width="14"
					fill="none"
				/>
				<circle
					cx="85"
					cy="85"
					r="70"
					:stroke="scoreColor"
					stroke-width="14"
					fill="none"
					stroke-linecap="round"
					class="score-ring"
					:style="{
						strokeDasharray: circumference,
						strokeDashoffset: dashOffset,
					}"
					transform="rotate(-90 85 85)"
				/>
			</svg>
			<div class="score-value">{{ seoScore }}%</div>
		</div>

		<p class="url-label">{{ targetUrl }}</p>
	</div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
	seoScore: {
		type: Number,
		default: null,
	},
	targetUrl: {
		type: String,
		default: '',
	},
});

const circumference = 2 * Math.PI * 70;

const dashOffset = computed(() =>
	props.seoScore !== null && props.seoScore !== undefined
		? circumference - (props.seoScore / 100) * circumference
		: circumference,
);

const scoreColor = computed(() => {
	const s = props.seoScore;
	if (s === null || s === undefined) return 'var(--primary)';
	if (s >= 80) return 'var(--good)';
	if (s >= 50) return '#f59e0b';
	return 'var(--bad)';
});
</script>

<style scoped>
.score-card {
	text-align: center;
}

.card-title {
	font-size: 24px;
	margin-bottom: 20px;
}

.score-wrapper {
	width: 170px;
	height: 170px;
	position: relative;
	margin: auto;
}

.score-value {
	inset: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 36px;
	font-weight: 700;
}

.score-ring {
	transition: stroke-dashoffset 0.9s ease;
}

.url-label {
	margin-top: 14px;
	color: var(--text);
	font-size: 14px;
	word-break: break-word;
}
</style>
