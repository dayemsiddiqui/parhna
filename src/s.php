<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Profile extends CI_Controller {

	/**
	 * Index Page for this controller.
	 *
	 * Maps to the following URL
	 * 		http://example.com/index.php/welcome
	 *	- or -
	 * 		http://example.com/index.php/welcome/index
	 *	- or -
	 * Since this controller is set as the default controller in
	 * config/routes.php, it's displayed at http://example.com/
	 *
	 * So any other public methods not prefixed with an underscore will
	 * map to /index.php/welcome/<method_name>
	 * @see https://codeigniter.com/user_guide/general/urls.html
	 */

	public function index(){
		$this->load->view('admin/base');
		$this->load->view('admin/index');
	}

	public function employee()
	{
		$this->load->database();
		$this->load->model('Employee_profile');
		$departments = $this->Employee_profile->get_all_departments();
		$designations = $this->Employee_profile->get_all_designations();
		$data = array(
			'departments' => $departments,
			'designations'=> $designations
	  );
		$this->load->view('admin/base');
		$this->load->view('admin/profileedit', $data);

	}

	public function designation()
	{
		$this->load->view('admin/base');
		$this->load->view('admin/designationedit');

	}

	public function department()
	{
		$this->load->view('admin/base');
		$this->load->view('admin/departmentedit');

	}

	public function designationinfo()
	{
		$this->load->database();
		$this->load->model('Employee_profile');
		$rowcount = $this->Employee_profile->get_row_count();
		$result = $this->Employee_profile->get_all_designations();
		$data = array(
								'rowcount' => $rowcount,
								'result' => $result
						);

		$this->load->view('admin/base');
		$this->load->view('admin/designationinfo', $data);

	}

	public function departmentinfo()
	{
		$this->load->database();
		$this->load->model('Employee_profile');
		$rowcount = $this->Employee_profile->get_row_count();
		$result = $this->Employee_profile->get_all_departments();
		$data = array(
								'rowcount' => $rowcount,
								'result' => $result
						);

		$this->load->view('admin/base');
		$this->load->view('admin/departmentinfo', $data);

	}

	public function employeeinfo()
	{
		$this->load->database();
		$this->load->model('Employee_profile');
		$rowcount = $this->Employee_profile->get_row_count();
		$result = $this->Employee_profile->get_all_users();
		$departments = $this->Employee_profile->get_all_departments();
		$designations = $this->Employee_profile->get_all_designations();
		$data = array(
                'rowcount' => $rowcount,
								'result' => $result,
								'departments' => $departments,
								'designations' => $designations,
            );

		$this->load->view('admin/base');
		$this->load->view('admin/profileinfo', $data);

	}

	public function adddepartment(){
		$this->load->database();
		$this->load->model('Employee_profile');

		$data = array(
			'department_name' => $this->input->post('department_name'),
		);

		$str = $this->Employee_profile->add_department($data);
		// $this->load->view('test', $str);
		redirect('Profile/departmentinfo');
	}

	public function adddesignation(){
		$this->load->database();
		$this->load->model('Employee_profile');

		$data = array(
			'designation_name' => $this->input->post('designation_name'),
		);

		$str = $this->Employee_profile->add_designation($data);
		// $this->load->view('test', $str);
		redirect('Profile/designationinfo');
	}

	public function addemployee(){
		$this->load->database();
		$this->load->model('Employee_profile');

		$data = array(
			"Name" => $this->input->post('name'),
			"fatherName" => $this->input->post('father_name'),
			"Gender" => $this->input->post('gender'),
			"cnic" => $this->input->post('cnic'),
			"dob" => $this->input->post('dob'),
			"identityMark" => $this->input->post('identity_mark'),
			"address" => $this->input->post('address'),
			"mobileNo" => $this->input->post('mobileNo'),
			"telephoneNo" => $this->input->post('telephoneNo'),
			"email" => $this->input->post('email'),
			"basic_salary" => $this->input->post('basic_salary'),
			"duty_hour" => $this->input->post('duty_hour'),
			"basic_salary" => $this->input->post('basic_salary'),
			"department_id" => $this->input->post('department_id'),
			"designation_id" => $this->input->post('designation_id'),
			"profileImage" => "132addsa",
			"image" => "132addsa",
		);

		$str = $this->Employee_profile->add_employee($data);
		// $this->load->view('test', $str);
		redirect('Profile/employeeinfo');
	}

}
