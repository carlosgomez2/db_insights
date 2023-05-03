import ApplicationController from './application_controller';

export default class extends ApplicationController {
  static targets = [];

  scrap() {
    fetch('/scrape', { method: 'GET' })
      .then(response => response.json())
      .then(data => {
        const { message, _code } = JSON.parse(data);
        this.constructor.toast(message);
      });
  }
}
