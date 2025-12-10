<template>
	<div>
		<!-- NAVBAR -->
		<LazyNavBar />

		<div class="container">
			<h1
				style="
					font-size: 40px;
					font-weight: 800;
					text-align: center;
					margin-bottom: 12px;
				"
			>
				SEO Audit Tool
			</h1>

			<p
				style="
					text-align: center;
					color: var(--text);
					margin-bottom: 40px;
					font-size: 17px;
				"
			>
				Analyze website SEO, structure, broken links, performance & more.
			</p>

			<!-- INPUT -->
			<LazyIndexAuditForm v-model="url" :loading="loading" @submit="runAudit" />

			<!-- ERROR -->
			<div
				v-if="error"
				class="bad"
				style="text-align: center; margin-bottom: 20px"
			>
				{{ error }}
			</div>

			<!-- RESULTS -->
			<div v-if="result">
				<LazyIndexAuditScore
					:seo-score="result.seo_score"
					:target-url="result.url"
				/>
				<LazyIndexAuditMetrics :result="result" />
				<LazyIndexAuditKeywords :keywords="result.keywords" />
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue';

// shared dark mode state (adds/removes `.dark` on <html>)
useDarkMode();

const url = ref('');
const result = ref(null);
const error = ref('');
const loading = ref(false);
const { public: publicConfig } = useRuntimeConfig();

/* RUN AUDIT */
async function runAudit() {
	error.value = '';
	result.value = null;

	if (!url.value) {
		error.value = 'Please enter a URL';
		return;
	}

	loading.value = true;

	try {
		const data = await $fetch(`${publicConfig.apiBase}/seo-audit`, {
			params: { url: url.value },
		});

		if (data.error) error.value = data.error;
		else result.value = data;
	} catch (err) {
		error.value = 'Unable to reach backend.';
	}

	loading.value = false;
}
</script>

<style scoped>
.score-ring {
	transition: stroke-dashoffset 0.9s ease;
}
</style>
