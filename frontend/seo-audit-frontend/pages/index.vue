<template>
	<div class="min-h-screen bg-gray-100 p-6">
		<!-- HEADER -->
		<div class="max-w-3xl mx-auto mb-10">
			<h1 class="text-4xl font-bold text-center mb-3">
				Advanced SEO Audit Tool
			</h1>
			<p class="text-center text-gray-600">
				Enter any URL and get a full in-depth SEO scan with performance, schema,
				broken link analysis and more.
			</p>
		</div>

		<!-- INPUT FORM -->
		<div class="max-w-xl mx-auto flex gap-3 mb-10">
			<input
				v-model="url"
				type="text"
				placeholder="https://example.com"
				class="flex-1 border rounded-lg p-3 shadow-sm"
			/>
			<button
				@click="runAudit"
				class="bg-blue-600 text-white px-6 py-3 rounded-lg shadow hover:bg-blue-700 disabled:bg-gray-400"
				:disabled="loading"
			>
				<span v-if="!loading">Analyze</span>
				<span v-else>Analyzing...</span>
			</button>
		</div>

		<!-- ERROR -->
		<div v-if="error" class="max-w-xl mx-auto mb-4 text-center text-red-600">
			{{ error }}
		</div>

		<!-- LOADING -->
		<div v-if="loading" class="text-center text-gray-600">
			Running audit... please wait.
		</div>

		<!-- RESULTS -->
		<div v-if="result" class="max-w-5xl mx-auto mt-10">
			<!-- SCORE -->
			<div class="bg-white p-6 rounded-xl shadow mb-10 text-center">
				<h2 class="text-2xl font-semibold mb-4">SEO Score</h2>

				<div class="flex justify-center">
					<div class="relative w-40 h-40">
						<!-- background circle -->
						<svg class="w-full h-full">
							<circle
								cx="80"
								cy="80"
								r="70"
								stroke="#e5e7eb"
								stroke-width="15"
								fill="transparent"
							/>

							<!-- animated score circle -->
							<circle
								cx="80"
								cy="80"
								r="70"
								:stroke="scoreColor"
								stroke-width="15"
								fill="transparent"
								stroke-linecap="round"
								:stroke-dasharray="circumference"
								:stroke-dashoffset="dashOffset"
								transform="rotate(-90 80 80)"
							/>
						</svg>

						<!-- score text -->
						<div
							class="absolute inset-0 flex items-center justify-center text-3xl font-bold"
						>
							{{ result.seo_score }}%
						</div>
					</div>
				</div>

				<p class="mt-3 text-gray-600 break-all text-sm">{{ result.url }}</p>
			</div>

			<!-- BASIC METRICS -->
			<div class="grid md:grid-cols-2 gap-6 mb-10">
				<AnalysisCard title="Title" :value="result.title" />
				<AnalysisCard
					title="Meta Description"
					:value="result.meta_description"
				/>
				<AnalysisCard title="H1 Tag" :value="result.h1" />

				<AnalysisCard title="Word Count" :value="result.word_count" />
				<AnalysisCard title="Internal Links" :value="result.internal_links" />
				<AnalysisCard title="External Links" :value="result.external_links" />

				<AnalysisCard
					title="Missing Image ALTs"
					:value="result.missing_image_alts"
					:bad="result.missing_image_alts > 0"
				/>

				<AnalysisCard title="Viewport Meta" :value="result.has_viewport_tag" />
				<AnalysisCard
					title="Robots.txt Found"
					:value="result.robots_txt_found"
				/>
				<AnalysisCard title="Sitemap Found" :value="result.sitemap_found" />
			</div>

			<!-- BROKEN LINKS -->
			<div
				v-if="result.broken_links"
				class="bg-white p-6 rounded-xl shadow mb-10"
			>
				<h2 class="text-xl font-semibold mb-4">Broken Links</h2>

				<p>
					<strong>Internal Good:</strong>
					{{ result.broken_links.internal_good }}
				</p>
				<p>
					<strong>External Good:</strong>
					{{ result.broken_links.external_good }}
				</p>

				<!-- INTERNAL BROKEN -->
				<div class="mt-4">
					<h3 class="font-semibold text-red-600">Internal Broken Links</h3>
					<ul v-if="result.broken_links.internal_broken?.length">
						<li
							v-for="link in result.broken_links.internal_broken"
							:key="link"
							class="text-red-700 text-sm"
						>
							{{ link }}
						</li>
					</ul>
					<p v-else class="text-green-600">None 🎉</p>
				</div>

				<!-- EXTERNAL BROKEN -->
				<div class="mt-4">
					<h3 class="font-semibold text-red-600">External Broken Links</h3>
					<ul v-if="result.broken_links.external_broken?.length">
						<li
							v-for="link in result.broken_links.external_broken"
							:key="link"
							class="text-red-700 text-sm"
						>
							{{ link }}
						</li>
					</ul>
					<p v-else class="text-green-600">None 🎉</p>
				</div>
			</div>

			<!-- STRUCTURED DATA -->
			<div
				v-if="result.structured_data"
				class="bg-white p-6 rounded-xl shadow mb-10"
			>
				<h2 class="text-xl font-semibold mb-4">Structured Data (Schema)</h2>

				<div v-if="result.structured_data.length">
					<div
						v-for="(item, idx) in result.structured_data"
						:key="idx"
						class="bg-gray-100 rounded p-3 text-sm font-mono mb-3 whitespace-pre-wrap"
					>
						{{ item }}
					</div>
				</div>
				<p v-else class="text-gray-600">No schema detected.</p>
			</div>

			<!-- PERFORMANCE -->
			<div
				v-if="result.performance"
				class="bg-white p-6 rounded-xl shadow mb-10"
			>
				<h2 class="text-xl font-semibold mb-3">Performance Insights</h2>

				<p><strong>Load Time:</strong> {{ result.load_time_seconds }}s</p>
				<p>
					<strong>Page Size:</strong>
					{{ result.performance.page_size_bytes }} bytes
				</p>
				<p><strong>Scripts:</strong> {{ result.performance.script_count }}</p>
				<p><strong>Images:</strong> {{ result.performance.image_count }}</p>
				<p><strong>DOM Nodes:</strong> {{ result.performance.dom_nodes }}</p>

				<h3 class="mt-4 font-semibold">Server Headers</h3>
				<pre class="text-sm bg-gray-100 p-3 rounded">{{
					result.performance.server_headers
				}}</pre>
			</div>

			<!-- KEYWORDS -->
			<div v-if="result.keywords" class="bg-white p-6 rounded-xl shadow mb-10">
				<h2 class="text-xl font-semibold mb-3">Top Keywords</h2>

				<div class="flex flex-wrap gap-3">
					<span
						v-for="item in result.keywords"
						:key="item.keyword"
						class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full"
					>
						{{ item.keyword }} ({{ item.count }})
					</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue';
import AnalysisCard from '../components/AnalysisCard.vue';

const BACKEND = 'https://seo-audit-tool-production-a57e.up.railway.app';

const url = ref('');
const result = ref(null);
const loading = ref(false);
const error = ref('');

// Score circle math
const circumference = 2 * Math.PI * 70;

const dashOffset = computed(() =>
	result.value
		? circumference - (result.value.seo_score / 100) * circumference
		: circumference,
);

const scoreColor = computed(() => {
	if (!result.value) return '#4f46e5';
	const s = result.value.seo_score;
	if (s >= 80) return '#10b981';
	if (s >= 50) return '#f59e0b';
	return '#ef4444';
});

async function runAudit() {
	error.value = '';
	result.value = null;

	if (!url.value.trim()) {
		error.value = 'Please enter a URL';
		return;
	}

	loading.value = true;

	try {
		const data = await $fetch(`${BACKEND}/seo-audit`, {
			params: { url: url.value },
		});

		if (data.error) error.value = data.error;
		else result.value = data;
	} catch (e) {
		error.value = 'Failed to contact backend.';
	}

	loading.value = false;
}
</script>
