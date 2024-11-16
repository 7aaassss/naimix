// Функция для создания звезд
function createStars() {
    const starContainer = document.querySelector('.animated-bg');
    const starCount = 150; // Увеличьте количество звезд

    for (let i = 0; i < starCount; i++) {
        const star = document.createElement('div');
        star.classList.add('stars');
        
        // Случайное позиционирование звезд
        star.style.top = Math.random() * 200 + '%';
        star.style.left = Math.random() * 100 + '%';

        // Добавляем звезду в контейнер
        starContainer.appendChild(star);
    }
}

// Вызов функции создания звезд при загрузке страницы
window.onload = () => {
    createStars();
    loadTeams();
};

// Функция загрузки команд
async function loadTeams() {
    try {
        const response = await fetch('/teams', { method: 'POST' });
        const result = await response.json();
        const teams = result.teams;

        const teamSelect = document.getElementById('team');
        teams.forEach(team => {
            const option = document.createElement('option');
            option.value = team.name;
            option.textContent = team.name;
            teamSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading teams:', error);
    }
}

document.getElementById('mainForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/date', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('response').textContent = JSON.stringify(result, null, 2);
});
