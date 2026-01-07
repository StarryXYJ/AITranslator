const translateBtn = document.getElementById('translateBtn');
const inputText = document.getElementById('inputText');
const resultSection = document.getElementById('resultSection');
const translationResult = document.getElementById('translationResult');
const keywordsResult = document.getElementById('keywordsResult');
const errorSection = document.getElementById('errorSection');
const errorMessage = document.getElementById('errorMessage');
const btnText = document.querySelector('.btn-text');
const loader = document.querySelector('.loader');

const API_URL = 'http://localhost:8000/translate';

translateBtn.addEventListener('click', async () => {
    const text = inputText.value.trim();

    if (!text) {
        showError('请输入要翻译的中文内容');
        return;
    }

    // Hide previous results
    resultSection.style.display = 'none';
    errorSection.style.display = 'none';

    // Show loading state
    translateBtn.disabled = true;
    btnText.style.display = 'none';
    loader.style.display = 'block';

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
        });

        if (!response.ok) {
            throw new Error('翻译请求失败');
        }

        const data = await response.json();

        // Display translation
        translationResult.textContent = data.translation;

        // Display keywords
        keywordsResult.innerHTML = '';
        data.keywords.forEach(keyword => {
            const chip = document.createElement('span');
            chip.className = 'keyword-chip';
            chip.textContent = keyword;
            keywordsResult.appendChild(chip);
        });

        // Show results
        resultSection.style.display = 'block';

    } catch (error) {
        showError(`错误: ${error.message}`);
    } finally {
        // Reset button state
        translateBtn.disabled = false;
        btnText.style.display = 'block';
        loader.style.display = 'none';
    }
});

function showError(message) {
    errorMessage.textContent = message;
    errorSection.style.display = 'block';
}

// Allow Enter key to trigger translation (Ctrl+Enter for textarea)
inputText.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        translateBtn.click();
    }
});
