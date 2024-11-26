<script lang="ts">
    // 停留所検索のロジック
    let searchQuery: string = ''; // ユーザーが入力した検索クエリ
    let stops: string[] = ['品川シーサイド', '鮫洲', '青物横丁', '大井町']; // 停留所データ
    let filteredStops: string[] = []; // フィルタリングされた候補リスト
    let selectedStop: string = ''; // 選択された停留所

    function searchStops() {
        if (searchQuery.length > 0) {
            filteredStops = stops.filter(stop =>
                stop.includes(searchQuery) // 入力値に含まれる停留所を検索
            );
        } else {
            filteredStops = [];
        }
    }

    function selectStop(stop: string) {
        selectedStop = stop; // 選択された停留所を保存
        filteredStops = []; // 候補リストをクリア
    }

    function goToCamera() {
        if (selectedStop) {
            goto("/qr")
        } else {
            alert('停留所を選択してください。');
        }
    }

	import { goto } from '$app/navigation';
    
    
</script>

<main class="container mx-auto p-4">
    <!-- 停留所検索 -->
    <section>
        <h1 class="text-2xl font-bold mb-4">停留所検索</h1>

        <!-- 検索バー -->
        <div class="relative">
            <input 
                type="text"
                class="input input-bordered w-full"
                bind:value={searchQuery}
                on:input={searchStops}
                placeholder="停留所を検索"
            />
            <!-- 検索候補の表示 -->
            {#if filteredStops.length > 0}
                <ul class="absolute left-0 mt-2 w-full bg-white border border-gray-200 rounded shadow-lg">
                    {#each filteredStops as stop}
                        <li>
                            <button 
                                class="block w-full text-left p-2 hover:bg-gray-100"
                                type="button"
                                on:click={() => selectStop(stop)}
                            >
                                {stop}
                            </button>
                        </li>
                    {/each}
                </ul>
            {/if}
        </div>

        <!-- 選択された停留所の表示 -->
        {#if selectedStop}
            <p class="mt-4">選択された停留所: <strong>{selectedStop}</strong></p>
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


   