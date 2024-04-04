const form = document.forms[0];
if (form) {
  form.onsubmit = function (event) {
    const id = form.id.value;
    const password = form.password.value;
    const ul = document.querySelector('ul');

    while (ul.firstChild) ul.removeChild(ul.firstChild);

    if (!id || !/^1[89]012[01][0-9]{3}$/.test(id)) {
      event.preventDefault();
      const li = document.createElement('li');
      if (!id) {
        li.textContent = 'Id is required';
        ul.appendChild(li);
      } else {
        li.textContent = 'Incorrect id format';
        ul.appendChild(li);
      }
    }

    if (!password || password.length < 8 || password.length > 30) {
      event.preventDefault();
      const li = document.createElement('li');
      if (!password) {
        li.textContent = 'Password is required';
        ul.appendChild(li);
      } else {
        li.textContent = 'Password must be 8-30 characters';
        ul.appendChild(li);
      }
    }
  };
}
