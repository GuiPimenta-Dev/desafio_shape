import { Form, Navbar, Button } from 'react-bootstrap';
import ListVessels from './components/ListVessels/ListVessels';
import './App.css';
import AppState from './context/AppState';
import SetToInactive from './components/SetToInactive/SetToInactive';
import RegisterVessel from './components/RegisterVessel/RegisterVessel';
import RegisterEquipment from './components/RegisterEquipment/RegisterEquipment';
import ToastResponse from './components/ToastResponse/ToastResponse';

function App() {
	return (
		<AppState>
			<div className='mt-5'>
				<Navbar fixed='top' bg='info' expand='lg'>
					<Navbar.Brand className='text-white' href='/'>
						Vessels Manager
					</Navbar.Brand>
					<Button
						className='button-react'
						href='https://shapechallenge.herokuapp.com/docs.html'
						target='_blank'>
						API Documentation
					</Button>
				</Navbar>
				<div className='container'>
					<div className='row'>
						<div className='col-6'>
							<Form>
								<RegisterVessel />
								<RegisterEquipment />
							</Form>
						</div>
						<div className='col-6'>
							<ListVessels />
						</div>
					</div>
					<div className='row mb-2'>
						<div className='col'>
							<SetToInactive />
						</div>
					</div>
				</div>
				<div className='footer'>Created By Guilherme Alves Pimenta</div>
			</div>
			<ToastResponse />
		</AppState>
	);
}

export default App;
