import { Controller } from 'stimulus';
import Toastify from 'toastify-js';

export default class extends Controller {
  static toast(message) {
    Toastify({
      text: message,
      gravity: 'top',
      position: 'center',
      duration: 3000
    }).showToast();
  }
}
