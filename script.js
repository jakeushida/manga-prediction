document.addEventListener('DOMContentLoaded', () => {
    const chapterInput = document.getElementById('chapterInput');
    const predictBtn = document.getElementById('predictBtn');
    const resultContainer = document.getElementById('resultContainer');
    const resultDate = document.getElementById('resultDate');
    const loading = document.getElementById('loading');

    // Model parameters state
    let modelParams = null;

    // Fetch the model parameters on load
    async function loadModelParameters() {
        try {
            const response = await fetch('model_parameters.json');
            if (!response.ok) {
                throw new Error('Could not load parameters');
            }
            modelParams = await response.json();
            console.log("Model parameters loaded successfully.");
        } catch (error) {
            console.error(error);
            predictBtn.textContent = 'Error Loading Data';
            predictBtn.disabled = true;
        }
    }

    // Function to calculate the predicted date
    function predictReleaseDate(chapter) {
        if (!modelParams) return null;

        const baseDate = new Date(modelParams.base_date);
        const intercept = modelParams.intercept;

        // In sklearn's PolynomialFeatures(degree=2), the coefficients array is [c0, c1, c2].
        // intercept handles c0, so we use indices 1 and 2 for the actual chapter values.
        const coef1 = modelParams.coefficients[1];
        const coef2 = modelParams.coefficients[2];

        // Apply polynomial regression formula
        // y = intercept + coef1*x + coef2*x^2
        const daysSinceFirstRelease = intercept + (coef1 * chapter) + (coef2 * Math.pow(chapter, 2));

        // Add the predicted days to the base date
        const predictedDate = new Date(baseDate.getTime() + (daysSinceFirstRelease * 24 * 60 * 60 * 1000));
        return predictedDate;
    }

    // Format date nicely
    function formatDate(date) {
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        return date.toLocaleDateString('en-US', options);
    }

    // Event listeners
    predictBtn.addEventListener('click', () => {
        const chapter = parseInt(chapterInput.value, 10);

        if (isNaN(chapter) || chapter <= 0) {
            alert('Please enter a valid positive chapter number.');
            return;
        }

        // Show loading state
        resultContainer.classList.add('hidden');
        loading.classList.remove('hidden');

        // Small delay to make interaction feel substantial
        setTimeout(() => {
            const predictedDate = predictReleaseDate(chapter);

            if (predictedDate) {
                resultDate.textContent = formatDate(predictedDate);
                loading.classList.add('hidden');
                resultContainer.classList.remove('hidden');
            }
        }, 400); // 400ms delay for UI smoothness
    });

    // Allow pressing "Enter" in the input field
    chapterInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            predictBtn.click();
        }
    });

    // Initialize application
    loadModelParameters();
});
