
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
		  <div class="row">
				<div class="col-lg-12">
					<h3 class="page-header"><i class="fa fa-user-md"></i> Profile</h3>
					<!-- <ol class="breadcrumb">
						<li><i class="fa fa-home"></i><a href="index.html">Home</a></li>
						<li><i class="icon_documents_alt"></i>Pages</li>
						<li><i class="fa fa-user-md"></i>Profile</li>
					</ol> -->
				</div>
			</div>
              <div class="row">
                <!-- profile-widget -->
                <div class="col-lg-12">
                    <section class="panel">
                          <header class="panel-heading">
                             Employee Details
                          </header>
                          <table class="table">
                              <thead>
                              <tr>

                                  <th>Name</th>
                                  <th>Father Name</th>
                                  <th>Gender</th>
                                  <th>CNIC</th>
                                  <th>Identity Mark</th>
                                  <th>Address</th>
                                  <th>Phone Number</th>
                                  <th>Mobile Number</th>
                                  <th>Email</th>
                                  <th>Basic Salary</th>
                                  <th>Duty Hours</th>
                                  <th>Department</th>
                                  <th>Designation</th>
                              </tr>
                              </thead>
                              <tbody>
                            <?php
                            foreach ($result as $row) {

                              echo "<tr>";
                                       echo "<td>";
                                       echo $row->Name;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->fatherName;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->Gender;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->cnic;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->identityMark;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->address;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->telephoneNo;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->mobileNo;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->email;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->basic_salary;
                                       echo "</td>";

                                       echo "<td>";
                                       echo $row->duty_hour;
                                       echo "</td>";

                                       echo "<td>";
                                       foreach ($departments as $department) {
                                         if($department->id == $row->department_id){
                                           echo $department->department_name;

                                         }
                                       }
                                       echo "</td>";

                                       echo "<td>";
                                       echo $designations[$row->designation_id]->designation_name;
                                       echo "</td>";






                              echo "</tr>";
                            }
                              ?>


                              </tbody>
                          </table>
                      </section>
                </div>
              </div>
          </section>
      </section>
      <!--main content end-->
