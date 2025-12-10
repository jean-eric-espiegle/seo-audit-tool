<template>
	<section class="card table-card">
		<div class="section-header">
			<h2>Broken Links</h2>
		</div>
		<div class="two-col">
			<div>
				<p class="eyebrow">Primary</p>
				<h4 class="site-title">{{ mainUrl }}</h4>
				<p class="counts">
					<strong>Internal broken:</strong> {{ internalMain }}
					<span class="dot">•</span>
					<strong>External broken:</strong> {{ externalMain }}
				</p>
				<ul class="small-list" v-if="(mainBroken?.internal_broken?.length || 0) > 0">
					<li v-for="link in mainBroken.internal_broken" :key="link">{{ link }}</li>
				</ul>
				<ul class="small-list" v-if="(mainBroken?.external_broken?.length || 0) > 0">
					<li v-for="link in mainBroken.external_broken" :key="link">{{ link }}</li>
				</ul>
			</div>
			<div>
				<p class="eyebrow">Competitor</p>
				<h4 class="site-title">{{ competitorUrl }}</h4>
				<p class="counts">
					<strong>Internal broken:</strong> {{ internalCompetitor }}
					<span class="dot">•</span>
					<strong>External broken:</strong> {{ externalCompetitor }}
				</p>
				<ul
					class="small-list"
					v-if="(competitorBroken?.internal_broken?.length || 0) > 0"
				>
					<li v-for="link in competitorBroken.internal_broken" :key="link">
						{{ link }}
					</li>
				</ul>
				<ul
					class="small-list"
					v-if="(competitorBroken?.external_broken?.length || 0) > 0"
				>
					<li v-for="link in competitorBroken.external_broken" :key="link">
						{{ link }}
					</li>
				</ul>
			</div>
		</div>
	</section>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
	mainUrl: String,
	competitorUrl: String,
	mainBroken: {
		type: Object,
		default: () => ({}),
	},
	competitorBroken: {
		type: Object,
		default: () => ({}),
	},
});

const internalMain = computed(() => props.mainBroken?.internal_broken?.length || 0);
const externalMain = computed(() => props.mainBroken?.external_broken?.length || 0);
const internalCompetitor = computed(
	() => props.competitorBroken?.internal_broken?.length || 0,
);
const externalCompetitor = computed(
	() => props.competitorBroken?.external_broken?.length || 0,
);
</script>

<style scoped>
.section-header h2 {
	margin-bottom: 12px;
}

.two-col {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
	gap: 16px;
}

.counts {
	margin-top: 6px;
	color: var(--text);
}

.dot {
	margin: 0 6px;
	color: var(--border);
}

.small-list {
	margin-top: 6px;
	display: grid;
	gap: 4px;
	font-size: 14px;
	padding-left: 18px;
	list-style: disc;
}

@media (max-width: 720px) {
	.two-col {
		grid-template-columns: 1fr;
	}
}
</style>
