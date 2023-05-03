import { Application } from 'stimulus';

// Import controllers
import DashboardController from './dashboard_controller';

const application = Application.start();

// Register controllers
application.register('dashboard', DashboardController);
