<script lang="ts">
    // 停留所検索のロジック
    let searchQuery: string = ''; // ユーザーが入力した検索クエリ
    let stops: StopData[];
    let filteredStops: StopData[] = []; // フィルタリングされた候補リスト
    let selectedStop: StopData|undefined = undefined; // 選択された停留所
    onMount(async () => {
        stops=await SearchService.searchSearch({searchWord:""})
    })
    async function searchStops() {
        if (searchQuery.length > 0) {
            filteredStops=await SearchService.searchSearch({searchWord:searchQuery})
            //filteredStops=stops.filter((v)=>v.name.includes(searchQuery))
        } else {
            filteredStops = [];
        }
    }

    function selectStop(stop: StopData) {
        selectedStop = stop; // 選択された停留所を保存
        searchQuery = stop.name;
        filteredStops = []; // 候補リストをクリア
    }

    function goToCamera() {
        if (selectedStop) {
            goto("/qr?dest_id="+selectedStop.stop_id)
        } else {
            showNotification({title:"Error",subtitle:'停留所を選択してください。',kind:"warn"});
        }
    }

	import { goto } from '$app/navigation';
	import { showNotification } from '$lib/notification';
	import { SearchService, type StopData } from '$lib/openapi';
	import { onMount } from 'svelte';
    
    
</script>

<main class="container mx-auto p-4">
    <!-- 停留所検索 -->
    <section>
        <h1 class="text-2xl font-bold mb-4">停留所検索</h1>

        <!-- 検索バー -->
        <div class="relative">
            <input 
                type="text"
                class="input input-bordered w-full dark:bg-black"
                bind:value={searchQuery}
                on:input={searchStops}
                placeholder="停留所を検索"
            />
            <!-- 検索候補の表示 -->
            {#if filteredStops.length > 0}
                <ul class="absolute left-0 mt-2 w-full bg-white dark:bg-black border border-gray-200 rounded shadow-lg">
                    {#each filteredStops as stop (stop.stop_id)}
                        <li>
                            <button 
                                class="block w-full text-left p-2 hover:bg-gray-100 dark:hover:text-black"
                                type="button"
                                on:click={() => selectStop(stop)}
                            >
                                {stop.name}
                            </button>
                        </li>
                    {/each}
                </ul>
            {/if}
        </div>

        <!-- 選択された停留所の表示 -->
        {#if selectedStop}
            <p class="mt-4">選択された停留所: <strong>{selectedStop.name}</strong></p>
        {/if}

        <!-- カメラを起動ボタン -->
        <button 
            class="btn btn-primary mt-4" 
            on:click={goToCamera}
        >
            カメラを起動
        </button>
    </section>
</main>


   