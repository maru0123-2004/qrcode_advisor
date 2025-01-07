<script lang="ts">
	import { goto } from "$app/navigation";
  import { Scanner } from "@peerpiper/qrcode-scanner-svelte";
  import type { PageData } from './$types';
	import { showNotification } from "$lib/notification";

	export let data: PageData;
  let result: string | null = null;
  let isLoading: boolean = false;
  /**
   * QRコードスキャン成功時の処理
   * @param {CustomEvent<string>} e - スキャンイベント
   */
  const successfulScan = async (e: CustomEvent<string>) => {
    result = e.detail; // スキャンしたQRコードのデータを格納
    if (result) {
        goto(`/result?dest_id=${data.dest_id}&qrdata=${result}`)
    }
  };

  /**
   * データベースを検索
   * @param {string} searchTerm - 検索する文字列
   * @returns {Promise<boolean>} - データが見つかったかどうか
   */
  const searchInDatabase = async (searchTerm: string): Promise<boolean> => {
    try {
      const response = await fetch(`/api/search?q=${encodeURIComponent(searchTerm)}`);
      if (!response.ok) {
        throw new Error(`HTTPエラー: ${response.status}`);
      }

      const data = await response.json();
      return data?.found ?? false;
    } catch (error) {
      console.error("検索中にエラーが発生しました:", error);
      showNotification({title:"Error",subtitle:"検索処理中に問題が発生しました。もう一度お試しください。",kind:"warn"});
      return false;
    }
  };

  /**
   * スキャン結果をリセット
   */
  const resetScan = () => {
    result = null;
  };
</script>

<main class="container">
  <section>
    <h1 class="title">QRコードスキャン</h1>

    <!-- QRコードスキャナー -->
    <Scanner on:successfulScan={successfulScan}>
      <div class="scanner-overlay">
        {#if isLoading}
          <p class="loading-text">検索中...</p>
        {/if}
        {#if result === null}
          <p class="instruction">QRコードをスキャンしてください。</p>
        {/if}
      </div>
    </Scanner>

    <!-- 結果と再スキャンボタン -->
    {#if result}
      <div class="result-container">
        <p class="result">スキャン結果: <strong>{result}</strong></p>
        <button class="btn-reset" on:click={resetScan}>再スキャン</button>
      </div>
    {/if}
  </section>
</main>

<style>
  .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 2rem;
    text-align: center;
  }

  .title {
    font-size: 1.8rem;
    margin-bottom: 1rem;
    color: #333;
  }

  .scanner-overlay {
    position: relative;
    border: 2px dashed #ccc;
    padding: 1rem;
    margin-top: 1rem;
    background-color: #f9f9f9;
  }

  .instruction {
    color: #666;
    font-size: 1.2rem;
  }

  .loading-text {
    color: #2563eb;
    font-size: 1.2rem;
    font-weight: bold;
  }

  .result-container {
    margin-top: 1rem;
  }

  .result {
    margin-bottom: 1rem;
    font-size: 1.2rem;
  }

  .btn-reset {
    background-color: #23cd00;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .btn-reset:hover {
    background-color: #39b300;
  }
</style>
